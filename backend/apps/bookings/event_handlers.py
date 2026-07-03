from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from apps.common.events import EventDispatcher
from .events import BookingConfirmed, BookingCancelled, SeatHoldExpired, WaitlistPromoted
from infrastructure.celery_tasks.notification_tasks import send_booking_confirmation_email, send_cancellation_email, send_waitlist_promotion_email
from infrastructure.celery_tasks.booking_tasks import process_waitlist_for_show

def _broadcast_seats(show_id, seat_ids, status):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"show_{show_id}",
        {"type": "seat_status_update", "seat_ids": seat_ids, "status": status}
    )

def on_booking_confirmed(event):
    send_booking_confirmation_email.delay(event.booking_id)
    _broadcast_seats(event.show_id, event.seat_ids, "BOOKED")

def on_booking_cancelled(event):
    send_cancellation_email.delay(event.booking_id, event.user_id)
    process_waitlist_for_show.delay(event.show_id)
    _broadcast_seats(event.show_id, event.seat_ids, "AVAILABLE")

def on_seat_hold_expired(event):
    process_waitlist_for_show.delay(event.show_id)
    _broadcast_seats(event.show_id, event.seat_ids, "AVAILABLE")

def on_waitlist_promoted(event):
    send_waitlist_promotion_email.delay(event.waitlist_entry_id)
    _broadcast_seats(event.show_id, event.seat_ids, "HELD")

def register_handlers():
    EventDispatcher.subscribe(BookingConfirmed, on_booking_confirmed)
    EventDispatcher.subscribe(BookingCancelled, on_booking_cancelled)
    EventDispatcher.subscribe(SeatHoldExpired, on_seat_hold_expired)
    EventDispatcher.subscribe(WaitlistPromoted, on_waitlist_promoted)
