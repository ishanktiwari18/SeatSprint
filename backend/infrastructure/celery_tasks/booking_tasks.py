from celery import shared_task
from apps.bookings.services import BookingService
from apps.waitlist.services import WaitlistService

@shared_task
def expire_stale_holds():
    BookingService.expire_stale_holds()

@shared_task
def process_waitlist_for_show(show_id):
    WaitlistService.process_promotion(show_id)
