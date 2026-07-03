from django.db import models
from django.core.validators import MinValueValidator
from apps.common.models import TimeStampedModel
from apps.accounts.models import User
from apps.venues.models import Venue, Seat

class Event(TimeStampedModel):
    class EventType(models.TextChoices):
        MOVIE = 'MOVIE', 'Movie'
        CONCERT = 'CONCERT', 'Concert'
        PLAY = 'PLAY', 'Play'
        OTHER = 'OTHER', 'Other'
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    event_type = models.CharField(max_length=20, choices=EventType.choices)
    organiser = models.ForeignKey(User, on_delete=models.PROTECT, related_name='events')
    poster_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table = 'events'
        indexes = [models.Index(fields=['event_type']), models.Index(fields=['is_active']), models.Index(fields=['organiser'])]

class Show(TimeStampedModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='shows')
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT, related_name='shows')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    doors_open = models.DateTimeField(null=True, blank=True)
    is_cancelled = models.BooleanField(default=False)
    class Meta:
        db_table = 'shows'
        indexes = [models.Index(fields=['start_time']), models.Index(fields=['event', 'start_time'])]

class PriceCategory(TimeStampedModel):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='price_categories')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    class Meta:
        db_table = 'price_categories'
        unique_together = [('show', 'name')]

class ShowSeat(TimeStampedModel):
    class SeatStatus(models.TextChoices):
        AVAILABLE = 'AVAILABLE', 'Available'
        HELD = 'HELD', 'Held'
        BOOKED = 'BOOKED', 'Booked'
        UNAVAILABLE = 'UNAVAILABLE', 'Unavailable'
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='show_seats')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='show_seats')
    price_category = models.ForeignKey(PriceCategory, on_delete=models.PROTECT, null=True, blank=True)
    status = models.CharField(max_length=15, choices=SeatStatus.choices, default=SeatStatus.AVAILABLE)
    held_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='held_seats')
    hold_expires_at = models.DateTimeField(null=True, blank=True)
    booked_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'show_seats'
        unique_together = [('show', 'seat')]
        indexes = [models.Index(fields=['show', 'status']), models.Index(fields=['held_by', 'hold_expires_at'])]
