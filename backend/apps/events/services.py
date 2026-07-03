from django.db import transaction
from .models import Event, Show, PriceCategory, ShowSeat
from apps.venues.models import Seat

class EventService:
    @staticmethod
    @transaction.atomic
    def create_event(organiser, title, description, event_type, poster_url=''):
        return Event.objects.create(organiser=organiser, title=title, description=description, event_type=event_type, poster_url=poster_url)

class ShowService:
    @staticmethod
    @transaction.atomic
    def create_show(event, venue, start_time, end_time, doors_open=None, price_categories=None):
        show = Show.objects.create(event=event, venue=venue, start_time=start_time, end_time=end_time, doors_open=doors_open)
        if price_categories:
            for pc in price_categories:
                PriceCategory.objects.create(show=show, name=pc['name'], price=pc['price'])
        seats = Seat.objects.filter(row__section__venue=venue, is_available=True)
        show_seats = [ShowSeat(show=show, seat=seat, status=ShowSeat.SeatStatus.AVAILABLE) for seat in seats]
        ShowSeat.objects.bulk_create(show_seats, batch_size=1000)
        return show

    @staticmethod
    def cancel_show(show):
        show.is_cancelled = True
        show.save(update_fields=['is_cancelled'])
