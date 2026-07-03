from django.contrib import admin
from .models import Venue, Section, Row, Seat

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'total_capacity')
    search_fields = ('name', 'city')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'sort_order')
    list_filter = ('venue',)

@admin.register(Row)
class RowAdmin(admin.ModelAdmin):
    list_display = ('row_label', 'section', 'sort_order')

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'row', 'seat_type', 'is_available')
    list_filter = ('seat_type', 'is_available')
