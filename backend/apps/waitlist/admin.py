from django.contrib import admin
from .models import WaitlistEntry

@admin.register(WaitlistEntry)
class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ('show','user','position','requested_seats','status','offer_expires_at')
    list_filter = ('status',)
