from django.db import models
from apps.common.models import TimeStampedModel
from apps.accounts.models import User
from apps.events.models import Show

class WaitlistEntry(TimeStampedModel):
    class WaitlistStatus(models.TextChoices):
        WAITING = 'WAITING', 'Waiting'
        OFFERED = 'OFFERED', 'Offered'
        EXPIRED = 'EXPIRED', 'Expired'
        PROMOTED = 'PROMOTED', 'Promoted'
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='waitlist_entries')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='waitlist_entries')
    position = models.PositiveIntegerField()
    requested_seats = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=15, choices=WaitlistStatus.choices, default=WaitlistStatus.WAITING)
    offer_expires_at = models.DateTimeField(null=True, blank=True)
    promoted_booking = models.OneToOneField('bookings.Booking', on_delete=models.SET_NULL, null=True, blank=True, related_name='waitlist_promotion')
    class Meta:
        db_table = 'waitlist_entries'
        unique_together = [('show', 'user')]
        indexes = [models.Index(fields=['show','status','position']), models.Index(fields=['offer_expires_at'])]
