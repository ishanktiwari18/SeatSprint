from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.common.permissions import IsAdmin
from .models import Venue
from .serializers import VenueSerializer, VenueCreateSerializer
from .services import VenueService

class VenueListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return VenueCreateSerializer
        return VenueSerializer
    def get_queryset(self):
        return Venue.objects.prefetch_related('sections__rows__seats').all()
    def create(self, request, *args, **kwargs):
        serializer = VenueCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        venue = VenueService.create_venue_with_layout(**serializer.validated_data)
        return Response(VenueSerializer(venue).data, status=status.HTTP_201_CREATED)

class VenueDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = Venue.objects.prefetch_related('sections__rows__seats').all()
    serializer_class = VenueSerializer
