from celery import shared_task
from .services import WaitlistService

@shared_task
def process_waitlist_promotions():
    pass

@shared_task
def expire_stale_offers():
    WaitlistService.expire_stale_offers()
