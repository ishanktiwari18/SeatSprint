from rest_framework import generics, permissions
from apps.common.permissions import IsOrganiser
from .models import Event, ShowSeat
from .serializers import EventSerializer, EventCreateSerializer, ShowSerializer, ShowSeatSerializer
from .services import EventService, ShowService
from .filters import EventFilter

class EventListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOrganiser]
    filterset_class = EventFilter
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EventCreateSerializer
        return EventSerializer
    def get_queryset(self):
        return Event.objects.filter(organiser=self.request.user).prefetch_related('shows__price_categories')
    def perform_create(self, serializer):
        serializer.save(organiser=self.request.user)

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOrganiser]
    queryset = Event.objects.prefetch_related('shows__price_categories')
    serializer_class = EventSerializer
    def get_queryset(self):
        return self.queryset.filter(organiser=self.request.user)

class ShowCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOrganiser]
    serializer_class = ShowSerializer
    def perform_create(self, serializer):
        event = Event.objects.get(id=self.request.data.get('event'))
        if event.organiser != self.request.user:
            self.permission_denied(self.request)
        ShowService.create_show(**serializer.validated_data)

class ShowSeatListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ShowSeatSerializer
    def get_queryset(self):
        show_id = self.kwargs['pk']
        return ShowSeat.objects.filter(show_id=show_id).select_related('seat__row__section').order_by('seat_id')

class CustomerEventListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EventSerializer
    queryset = Event.objects.filter(is_active=True).prefetch_related('shows__price_categories')
    filterset_class = EventFilter
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']
