from rest_framework import generics, status, permissions
from rest_framework.response import Response
from apps.common.permissions import IsCustomer
from apps.common.exceptions import SeatsUnavailableException, InvalidStateTransition, BusinessException
from .services import BookingService
from .serializers import BookingSerializer, BookingInitiateSerializer, BookingCancelSerializer
from .models import Booking
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

@method_decorator(ratelimit(key='user', rate='20/m', method='POST'), name='post')
class BookingInitiateView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsCustomer]
    serializer_class = BookingInitiateSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            booking = BookingService.initiate_booking(user=request.user, show_id=serializer.validated_data['show_id'], seat_ids=serializer.validated_data['seat_ids'])
        except (SeatsUnavailableException, BusinessException) as e:
            return Response({'error': str(e)}, status=status.HTTP_409_CONFLICT)
        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

class BookingConfirmView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsCustomer]
    serializer_class = BookingSerializer
    def post(self, request, pk):
        try:
            booking = BookingService.confirm_booking(booking_id=pk, user=request.user)
        except PermissionError as e:
            return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)
        except InvalidStateTransition as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(BookingSerializer(booking).data)

class BookingCancelView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsCustomer]
    serializer_class = BookingCancelSerializer
    def post(self, request, pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            booking = BookingService.cancel_booking(booking_id=pk, user=request.user, reason=serializer.validated_data.get('reason',''))
        except (PermissionError, InvalidStateTransition) as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(BookingSerializer(booking).data)

class BookingListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookingSerializer
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).prefetch_related('items__show_seat__seat__row__section').order_by('-created_at')
