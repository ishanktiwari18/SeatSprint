from django.contrib import admin
from .models import Event, Show, PriceCategory, ShowSeat

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'organiser', 'is_active')
    list_filter = ('event_type', 'is_active')
    search_fields = ('title',)

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('event', 'venue', 'start_time', 'is_cancelled')
    list_filter = ('is_cancelled',)

@admin.register(PriceCategory)
class PriceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'show', 'price')

@admin.register(ShowSeat)
class ShowSeatAdmin(admin.ModelAdmin):
    list_display = ('show', 'seat', 'status', 'held_by')
    list_filter = ('status',)
    raw_id_fields = ('held_by',)
