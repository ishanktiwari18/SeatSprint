from django.db.models import Sum
from apps.bookings.models import Booking
from apps.payments.models import Payment

def get_admin_dashboard():
    total_bookings = Booking.objects.count()
    total_revenue = Payment.objects.filter(status='SUCCESS').aggregate(Sum('amount'))['amount__sum'] or 0
    return {'total_bookings': total_bookings, 'total_revenue': str(total_revenue)}

def get_organiser_dashboard(organiser):
    shows = organiser.events.all().values_list('shows', flat=True)
    bookings = Booking.objects.filter(show__in=shows).count()
    revenue = Payment.objects.filter(booking__show__in=shows, status='SUCCESS').aggregate(Sum('amount'))['amount__sum'] or 0
    return {'total_bookings': bookings, 'total_revenue': str(revenue)}
