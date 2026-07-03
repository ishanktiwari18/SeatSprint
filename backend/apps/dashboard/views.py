from rest_framework import generics, permissions
from rest_framework.response import Response
from apps.common.permissions import IsAdmin, IsOrganiser
from .queries import get_admin_dashboard, get_organiser_dashboard

class AdminDashboardView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    def get(self, request):
        data = get_admin_dashboard()
        return Response(data)

class OrganiserDashboardView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOrganiser]
    def get(self, request):
        data = get_organiser_dashboard(request.user)
        return Response(data)
