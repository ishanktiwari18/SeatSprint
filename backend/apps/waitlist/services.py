from django.db import transaction, models
from django.utils import timezone
from apps.common.events import EventDispatcher
from apps.events.models import Show, ShowSeat
from apps.bookings.models import Booking, BookingItem
from apps.bookings.state_service import BookingStateService
from apps.bookings.events import WaitlistPromoted
from .models import WaitlistEntry

class WaitlistService:
    @staticmethod
    def signup(user, show_id, requested_seats=1):
        show = Show.objects.get(id=show_id)
        with transaction.atomic():
            last_entry = WaitlistEntry.objects.filter(show=show).order_by('-position').first()
            position = last_entry.position + 1 if last_entry else 1
            entry = WaitlistEntry.objects.create(show=show, user=user, position=position, requested_seats=requested_seats, status='WAITING')
            return entry

    @staticmethod
    @transaction.atomic
    def process_promotion(show_id):
        show = Show.objects.get(id=show_id)
        available_seats = list(ShowSeat.objects.select_for_update().filter(show=show, status=ShowSeat.SeatStatus.AVAILABLE).order_by('seat_id'))
        if not available_seats:
            return
        waiting_entries = WaitlistEntry.objects.select_for_update(skip_locked=True).filter(show=show, status='WAITING').order_by('position')
        for entry in waiting_entries:
            needed = entry.requested_seats
            if len(available_seats) < needed:
                needed = len(available_seats)
            if needed == 0:
                break
            allocated = available_seats[:needed]
            del available_seats[:needed]
            booking = Booking.objects.create(user=entry.user, show=show, status='INITIATED', total_amount=0)
            BookingStateService.transition_to(booking, 'HELD')
            for seat in allocated:
                seat.status = ShowSeat.SeatStatus.HELD
                seat.held_by = entry.user
                seat.hold_expires_at = timezone.now() + timezone.timedelta(minutes=10)
                seat.save(update_fields=['status','held_by','hold_expires_at'])
                BookingItem.objects.create(booking=booking, show_seat=seat, price=0)
            entry.status = 'OFFERED'
            entry.offer_expires_at = timezone.now() + timezone.timedelta(minutes=10)
            entry.promoted_booking = booking
            entry.save()
            EventDispatcher.dispatch(WaitlistPromoted(str(entry.id), str(entry.user.id), str(show.id), [str(s.seat_id) for s in allocated]))
        transaction.on_commit(EventDispatcher.flush)

    @staticmethod
    @transaction.atomic
    def expire_stale_offers():
        now = timezone.now()
        expired_entries = WaitlistEntry.objects.select_for_update(skip_locked=True).filter(status='OFFERED', offer_expires_at__lte=now)
        for entry in expired_entries:
            booking = entry.promoted_booking
            if booking and booking.status == 'HELD':
                BookingStateService.transition_to(booking, 'EXPIRED')
                for item in booking.items.all():
                    seat = item.show_seat
                    seat.status = ShowSeat.SeatStatus.AVAILABLE
                    seat.held_by = None
                    seat.hold_expires_at = None
                    seat.save(update_fields=['status','held_by','hold_expires_at'])
            entry.status = 'EXPIRED'
            entry.save()
