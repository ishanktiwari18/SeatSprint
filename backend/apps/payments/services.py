from django.db import transaction
from django.utils import timezone
from .models import Payment
from apps.bookings.services import BookingService

class PaymentService:
    @staticmethod
    @transaction.atomic
    def create_payment(booking):
        total = sum(item.price for item in booking.items.all())
        payment = Payment.objects.create(booking=booking, user=booking.user, amount=total, currency='INR', status=Payment.PaymentStatus.PENDING, payment_url=f"https://pay.seatsprint.com/pay/{booking.booking_number}")
        return payment

    @staticmethod
    @transaction.atomic
    def handle_callback(payment_id, success, gateway_tx_id=''):
        payment = Payment.objects.select_for_update().get(id=payment_id)
        if payment.status != Payment.PaymentStatus.PENDING:
            return payment
        booking_id = payment.booking_id
        if success:
            payment.status = Payment.PaymentStatus.SUCCESS
            payment.gateway_transaction_id = gateway_tx_id
            payment.paid_at = timezone.now()
            payment.save()
            BookingService.process_payment_callback(str(booking_id), success=True, gateway_tx_id=gateway_tx_id)
        else:
            payment.status = Payment.PaymentStatus.FAILED
            payment.save()
            BookingService.process_payment_callback(str(booking_id), success=False)
        return payment

    @staticmethod
    @transaction.atomic
    def refund_payment(payment):
        if payment.status != Payment.PaymentStatus.SUCCESS:
            raise ValueError("Only successful payments can be refunded.")
        payment.status = Payment.PaymentStatus.REFUNDED
        payment.save()
        return payment
