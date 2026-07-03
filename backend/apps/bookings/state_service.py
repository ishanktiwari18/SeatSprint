from django.utils import timezone
from .models import Booking
from apps.common.exceptions import InvalidStateTransition

TRANSITION_MAP = {
    None: ['INITIATED'],
    'INITIATED': ['HELD', 'FAILED'],
    'HELD': ['PAYMENT_PENDING', 'EXPIRED', 'FAILED'],
    'PAYMENT_PENDING': ['CONFIRMED', 'FAILED'],
    'CONFIRMED': ['CANCELLED'],
    'EXPIRED': [],
    'FAILED': [],
    'CANCELLED': [],
}

class BookingStateService:
    @staticmethod
    def transition_to(booking: Booking, new_status: str, reason: str = None) -> Booking:
        allowed = TRANSITION_MAP.get(booking.status, [])
        if new_status not in allowed:
            raise InvalidStateTransition(f"Cannot transition from {booking.status} to {new_status}")
        now = timezone.now()
        booking.status = new_status
        if new_status == 'CONFIRMED':
            booking.booked_at = now
        elif new_status == 'CANCELLED':
            booking.cancelled_at = now
            booking.cancellation_reason = reason or ''
        booking.save(update_fields=['status','booked_at','cancelled_at','cancellation_reason','updated_at'])
        return booking
