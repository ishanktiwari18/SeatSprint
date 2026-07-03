from django.urls import path
from .views import PaymentCallbackView

urlpatterns = [
    path('payments/<uuid:payment_id>/callback/', PaymentCallbackView.as_view(), name='payment-callback'),
]
