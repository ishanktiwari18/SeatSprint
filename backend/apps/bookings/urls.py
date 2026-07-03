from django.urls import path
from .views import BookingInitiateView, BookingConfirmView, BookingCancelView, BookingListView

urlpatterns = [
    path('bookings/initiate/', BookingInitiateView.as_view(), name='booking-initiate'),
    path('bookings/<uuid:pk>/confirm/', BookingConfirmView.as_view(), name='booking-confirm'),
    path('bookings/<uuid:pk>/cancel/', BookingCancelView.as_view(), name='booking-cancel'),
    path('bookings/', BookingListView.as_view(), name='booking-list'),
]
