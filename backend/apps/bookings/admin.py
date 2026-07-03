from django.contrib import admin
from .models import Booking, BookingItem

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_number','user','show','status','total_amount','created_at')
    list_filter = ('status',)
    search_fields = ('booking_number','user__email')

@admin.register(BookingItem)
class BookingItemAdmin(admin.ModelAdmin):
    list_display = ('booking','show_seat','price')
