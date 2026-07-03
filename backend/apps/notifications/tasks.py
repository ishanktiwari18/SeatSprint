from celery import shared_task

@shared_task
def send_booking_confirmation_email(booking_id):
    pass

@shared_task
def send_cancellation_email(booking_id, user_id):
    pass

@shared_task
def send_waitlist_promotion_email(entry_id):
    pass
