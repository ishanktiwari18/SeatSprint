from rest_framework import generics, status, permissions
from rest_framework.response import Response
from apps.common.permissions import IsCustomer
from .serializers import WaitlistJoinSerializer, WaitlistEntrySerializer
from .services import WaitlistService
from .models import WaitlistEntry

class WaitlistJoinView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsCustomer]
    serializer_class = WaitlistJoinSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        entry = WaitlistService.signup(user=request.user, show_id=serializer.validated_data['show_id'], requested_seats=serializer.validated_data.get('requested_seats',1))
        return Response(WaitlistEntrySerializer(entry).data, status=status.HTTP_201_CREATED)

class WaitlistStatusView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WaitlistEntrySerializer
    def get_queryset(self):
        return WaitlistEntry.objects.filter(user=self.request.user).order_by('-created_at')
