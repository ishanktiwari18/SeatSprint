from django.db import models
from apps.common.models import TimeStampedModel
from apps.accounts.models import User

class NotificationLog(TimeStampedModel):
    class NotificationType(models.TextChoices):
        BOOKING_CONFIRMATION = 'BOOKING_CONFIRMATION', 'Booking Confirmation'
        BOOKING_CANCELLATION = 'BOOKING_CANCELLATION', 'Booking Cancellation'
        WAITLIST_PROMOTION = 'WAITLIST_PROMOTION', 'Waitlist Promotion'
        HOLD_EXPIRY = 'HOLD_EXPIRY', 'Hold Expiry'
        PAYMENT_RECEIPT = 'PAYMENT_RECEIPT', 'Payment Receipt'
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_logs')
    notification_type = models.CharField(max_length=30, choices=NotificationType.choices)
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=200)
    body = models.TextField()
    status = models.CharField(max_length=20, choices=[('SENT','Sent'),('FAILED','Failed'),('PENDING','Pending')], default='PENDING')
    sent_at = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(blank=True)
    reference_id = models.UUIDField(null=True, blank=True)
    class Meta:
        db_table = 'notification_logs'
        indexes = [models.Index(fields=['user','notification_type']), models.Index(fields=['status'])]
