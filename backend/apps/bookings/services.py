from decimal import Decimal
from datetime import timedelta
from django.db import transaction, models
from django.utils import timezone
from apps.common.events import EventDispatcher
from apps.common.exceptions import SeatsUnavailableException, ShowCancelledException
from apps.events.models import Show, ShowSeat
from apps.accounts.models import User
from .models import Booking, BookingItem
from .state_service import BookingStateService, InvalidStateTransition
from .events import BookingConfirmed, BookingCancelled, SeatHoldExpired

class BookingService:
    HOLD_DURATION_MINUTES = 10

    @staticmethod
    def _lock_seats(show, seat_ids):
        seats = ShowSeat.objects.select_for_update().filter(show=show, seat_id__in=seat_ids).order_by('seat_id')
        if len(seats) != len(seat_ids):
            raise SeatsUnavailableException("One or more seats do not exist.")
        unavailable = [s for s in seats if s.status != ShowSeat.SeatStatus.AVAILABLE]
        if unavailable:
            raise SeatsUnavailableException(f"Seats {[str(s.seat_id) for s in unavailable]} are not available.")
        return seats

    @staticmethod
    @transaction.atomic
    def initiate_booking(user, show_id, seat_ids):
        show = Show.objects.get(id=show_id)
        if show.is_cancelled:
            raise ShowCancelledException()
        seats = BookingService._lock_seats(show, seat_ids)
        booking = Booking.objects.create(user=user, show=show, status='INITIATED', total_amount=Decimal('0.00'))
        BookingStateService.transition_to(booking, 'INITIATED')
        hold_expiry = timezone.now() + timedelta(minutes=BookingService.HOLD_DURATION_MINUTES)
        for seat in seats:
            seat.status = ShowSeat.SeatStatus.HELD
            seat.held_by = user
            seat.hold_expires_at = hold_expiry
            seat.save(update_fields=['status','held_by','hold_expires_at'])
            BookingItem.objects.create(booking=booking, show_seat=seat, price=Decimal('0.00'))
        BookingStateService.transition_to(booking, 'HELD')
        return booking

    @staticmethod
    @transaction.atomic
    def confirm_booking(booking_id, user):
        booking = Booking.objects.select_for_update().get(id=booking_id)
        if booking.user != user:
            raise PermissionError("Not your booking.")
        if booking.status != 'HELD':
            raise InvalidStateTransition("Booking is not in HELD state.")
        BookingStateService.transition_to(booking, 'PAYMENT_PENDING')
        return booking

    @staticmethod
    @transaction.atomic
    def process_payment_callback(booking_id, success, gateway_tx_id=''):
        booking = Booking.objects.select_for_update().get(id=booking_id)
        if booking.status != 'PAYMENT_PENDING':
            return booking
        if success:
            BookingStateService.transition_to(booking, 'CONFIRMED')
            show_seats = [item.show_seat for item in booking.items.all()]
            for seat in show_seats:
                seat.status = ShowSeat.SeatStatus.BOOKED
                seat.held_by = None
                seat.hold_expires_at = None
                seat.booked_at = timezone.now()
                seat.save(update_fields=['status','held_by','hold_expires_at','booked_at'])
            booking.total_amount = sum(item.price for item in booking.items.all())
            booking.save(update_fields=['total_amount'])
            EventDispatcher.dispatch(BookingConfirmed(str(booking.id), str(booking.user.id), str(booking.show.id), [str(s.seat_id) for s in show_seats]))
        else:
            BookingStateService.transition_to(booking, 'FAILED')
            show_seats = [item.show_seat for item in booking.items.all()]
            for seat in show_seats:
                seat.status = ShowSeat.SeatStatus.AVAILABLE
                seat.held_by = None
                seat.hold_expires_at = None
                seat.save(update_fields=['status','held_by','hold_expires_at'])
        transaction.on_commit(EventDispatcher.flush)
        return booking

    @staticmethod
    @transaction.atomic
    def cancel_booking(booking_id, user, reason=''):
        booking = Booking.objects.select_for_update().get(id=booking_id)
        if booking.user != user:
            raise PermissionError("Not your booking.")
        if booking.status != 'CONFIRMED':
            raise InvalidStateTransition("Only CONFIRMED bookings can be cancelled.")
        BookingStateService.transition_to(booking, 'CANCELLED', reason)
        show_seats = [item.show_seat for item in booking.items.all()]
        for seat in show_seats:
            seat.status = ShowSeat.SeatStatus.AVAILABLE
            seat.held_by = None
            seat.hold_expires_at = None
            seat.booked_at = None
            seat.save(update_fields=['status','held_by','hold_expires_at','booked_at'])
        EventDispatcher.dispatch(BookingCancelled(str(booking.id), str(user.id), str(booking.show.id), [str(s.seat_id) for s in show_seats]))
        transaction.on_commit(EventDispatcher.flush)
        return booking

    @staticmethod
    @transaction.atomic
    def expire_stale_holds():
        now = timezone.now()
        expired_seats = ShowSeat.objects.select_for_update(skip_locked=True).filter(
            status=ShowSeat.SeatStatus.HELD, hold_expires_at__lte=now
        ).select_related('held_by')
        for seat in expired_seats:
            booking_item = seat.booking_item
            if booking_item:
                booking = booking_item.booking
                if booking.status == 'HELD':
                    BookingStateService.transition_to(booking, 'EXPIRED')
                    EventDispatcher.dispatch(SeatHoldExpired(str(booking.id), str(booking.show.id), [str(seat.seat_id)]))
            seat.status = ShowSeat.SeatStatus.AVAILABLE
            seat.held_by = None
            seat.hold_expires_at = None
            seat.save(update_fields=['status','held_by','hold_expires_at'])
        transaction.on_commit(EventDispatcher.flush)
