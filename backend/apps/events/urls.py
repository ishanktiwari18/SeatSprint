from django.urls import path
from .views import EventListCreateView, EventDetailView, ShowCreateView, ShowSeatListView, CustomerEventListView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list'),
    path('events/<uuid:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('shows/', ShowCreateView.as_view(), name='show-create'),
    path('public/events/', CustomerEventListView.as_view(), name='public-event-list'),
    path('shows/<uuid:pk>/seats/', ShowSeatListView.as_view(), name='show-seats'),
]
