from django.db import models
from apps.common.models import TimeStampedModel

class Venue(TimeStampedModel):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    total_capacity = models.PositiveIntegerField(default=0)
    class Meta:
        db_table = 'venues'
        indexes = [models.Index(fields=['city', 'state'])]

class Section(TimeStampedModel):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=50)
    sort_order = models.PositiveSmallIntegerField(default=0)
    class Meta:
        db_table = 'sections'
        unique_together = [('venue', 'name')]
        ordering = ['sort_order']

class Row(TimeStampedModel):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='rows')
    row_label = models.CharField(max_length=10)
    sort_order = models.PositiveSmallIntegerField(default=0)
    class Meta:
        db_table = 'rows'
        unique_together = [('section', 'row_label')]
        ordering = ['sort_order']

class Seat(TimeStampedModel):
    row = models.ForeignKey(Row, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    seat_type = models.CharField(max_length=20, choices=[('REGULAR','Regular'),('VIP','VIP'),('WHEELCHAIR','Wheelchair')], default='REGULAR')
    is_available = models.BooleanField(default=True)
    class Meta:
        db_table = 'seats'
        unique_together = [('row', 'seat_number')]
