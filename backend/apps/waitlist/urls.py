from django.urls import path
from .views import WaitlistJoinView, WaitlistStatusView

urlpatterns = [
    path('waitlist/join/', WaitlistJoinView.as_view(), name='waitlist-join'),
    path('waitlist/', WaitlistStatusView.as_view(), name='waitlist-status'),
]
