import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings
import os

def generate_qr_code(booking):
    data = f"https://seatsprint.com/tickets/{booking.booking_number}"
    img = qrcode.make(data)
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    filename = f"qrcodes/{booking.booking_number}.png"
    from django.core.files.storage import default_storage
    file_path = default_storage.save(os.path.join(settings.MEDIA_ROOT, filename), ContentFile(buffer.getvalue()))
    booking.qr_code_url = settings.MEDIA_URL + filename
    booking.save(update_fields=['qr_code_url'])
    return booking.qr_code_url
