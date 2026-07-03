from apps.common.events import DomainEvent

class BookingConfirmed(DomainEvent):
    def __init__(self, booking_id, user_id, show_id, seat_ids):
        self.booking_id = booking_id
        self.user_id = user_id
        self.show_id = show_id
        self.seat_ids = seat_ids

class BookingCancelled(DomainEvent):
    def __init__(self, booking_id, user_id, show_id, seat_ids):
        self.booking_id = booking_id
        self.user_id = user_id
        self.show_id = show_id
        self.seat_ids = seat_ids

class SeatHoldExpired(DomainEvent):
    def __init__(self, booking_id, show_id, seat_ids):
        self.booking_id = booking_id
        self.show_id = show_id
        self.seat_ids = seat_ids

class WaitlistPromoted(DomainEvent):
    def __init__(self, waitlist_entry_id, user_id, show_id, seat_ids):
        self.waitlist_entry_id = waitlist_entry_id
        self.user_id = user_id
        self.show_id = show_id
        self.seat_ids = seat_ids
