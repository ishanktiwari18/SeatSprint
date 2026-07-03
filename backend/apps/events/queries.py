from django.db.models import Prefetch
from .models import Show, ShowSeat

def get_show_with_seats(show_id):
    return Show.objects.filter(id=show_id).prefetch_related(
        Prefetch('show_seats', queryset=ShowSeat.objects.select_related('seat__row__section'))
    ).first()

def get_available_seats(show_id):
    return ShowSeat.objects.filter(show_id=show_id, status=ShowSeat.SeatStatus.AVAILABLE).select_related('seat__row__section').order_by('seat_id')
