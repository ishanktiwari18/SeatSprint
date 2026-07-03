import uuid
from django.db import models
from apps.common.models import TimeStampedModel
from apps.accounts.models import User
from apps.events.models import Show, ShowSeat

def generate_booking_number():
    return uuid.uuid4().hex[:12].upper()

class Booking(TimeStampedModel):
    class BookingStatus(models.TextChoices):
        INITIATED = 'INITIATED', 'Initiated'
        HELD = 'HELD', 'Held'
        PAYMENT_PENDING = 'PAYMENT_PENDING', 'Payment Pending'
        CONFIRMED = 'CONFIRMED', 'Confirmed'
        CANCELLED = 'CANCELLED', 'Cancelled'
        EXPIRED = 'EXPIRED', 'Expired'
        FAILED = 'FAILED', 'Failed'
    booking_number = models.CharField(max_length=12, unique=True, default=generate_booking_number)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='bookings')
    show = models.ForeignKey(Show, on_delete=models.PROTECT, related_name='bookings')
    status = models.CharField(max_length=20, choices=BookingStatus.choices, default=BookingStatus.INITIATED)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    booked_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    cancellation_reason = models.TextField(blank=True)
    qr_code_url = models.URLField(blank=True)
    class Meta:
        db_table = 'bookings'
        indexes = [models.Index(fields=['user','status']), models.Index(fields=['show','status']), models.Index(fields=['booking_number'])]

class BookingItem(TimeStampedModel):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='items')
    show_seat = models.OneToOneField(ShowSeat, on_delete=models.PROTECT, related_name='booking_item', unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = 'booking_items'
        unique_together = [('booking', 'show_seat')]
