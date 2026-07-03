from django.core.mail import send_mail
from django.conf import settings
from .models import NotificationLog


def log_notification(
    user,
    notification_type,
    recipient_email,
    subject,
    body,
    reference_id=None,
    status="PENDING",
):
    return NotificationLog.objects.create(
        user=user,
        notification_type=notification_type,
        recipient_email=recipient_email,
        subject=subject,
        body=body,
        status=status,
        reference_id=reference_id,
    )


def _send_email(user, recipient_email, subject, body, notification_type, reference_id=None):
    try:
        send_mail(
            subject=subject,
            message=body,
            from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None),
            recipient_list=[recipient_email],
            fail_silently=False,
        )

        log_notification(
            user=user,
            notification_type=notification_type,
            recipient_email=recipient_email,
            subject=subject,
            body=body,
            reference_id=reference_id,
            status="SENT",
        )

    except Exception:
        log_notification(
            user=user,
            notification_type=notification_type,
            recipient_email=recipient_email,
            subject=subject,
            body=body,
            reference_id=reference_id,
            status="FAILED",
        )
        raise


def send_booking_confirmation_email(user, booking):
    subject = "Booking Confirmed"
    body = f"Your booking #{booking.id} has been confirmed."
    _send_email(
        user=user,
        recipient_email=user.email,
        subject=subject,
        body=body,
        notification_type="BOOKING_CONFIRMATION",
        reference_id=str(booking.id),
    )


def send_cancellation_email(user, booking):
    subject = "Booking Cancelled"
    body = f"Your booking #{booking.id} has been cancelled."
    _send_email(
        user=user,
        recipient_email=user.email,
        subject=subject,
        body=body,
        notification_type="BOOKING_CANCELLATION",
        reference_id=str(booking.id),
    )


def send_waitlist_promotion_email(user, booking):
    subject = "Seat Available"
    body = f"You have been promoted from the waitlist for booking #{booking.id}."
    _send_email(
        user=user,
        recipient_email=user.email,
        subject=subject,
        body=body,
        notification_type="WAITLIST_PROMOTION",
        reference_id=str(booking.id),
    )