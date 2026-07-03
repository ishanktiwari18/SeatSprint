from django.urls import path
from .views import AdminDashboardView, OrganiserDashboardView

urlpatterns = [
    path('dashboard/admin/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('dashboard/organiser/', OrganiserDashboardView.as_view(), name='organiser-dashboard'),
]
