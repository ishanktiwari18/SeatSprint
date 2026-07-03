from django.urls import path
from .views import VenueListCreateView, VenueDetailView

urlpatterns = [
    path('venues/', VenueListCreateView.as_view(), name='venue-list'),
    path('venues/<uuid:pk>/', VenueDetailView.as_view(), name='venue-detail'),
]
