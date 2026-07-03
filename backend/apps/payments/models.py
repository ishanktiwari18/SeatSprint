from django.db import models
from apps.common.models import TimeStampedModel
from apps.accounts.models import User

class Payment(TimeStampedModel):
    class PaymentStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        SUCCESS = 'SUCCESS', 'Success'
        FAILED = 'FAILED', 'Failed'
        REFUNDED = 'REFUNDED', 'Refunded'
    booking = models.ForeignKey('bookings.Booking', on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='INR')
    status = models.CharField(max_length=15, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    gateway_transaction_id = models.CharField(max_length=100, blank=True, unique=True, null=True)
    payment_method = models.CharField(max_length=20, blank=True)
    payment_url = models.URLField(blank=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'payments'
        indexes = [models.Index(fields=['status']), models.Index(fields=['booking','status']), models.Index(fields=['gateway_transaction_id'])]
