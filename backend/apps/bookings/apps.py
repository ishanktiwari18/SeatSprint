from django.apps import AppConfig

class BookingsConfig(AppConfig):
    name = 'apps.bookings'
    label = 'bookings'
    def ready(self):
        from .event_handlers import register_handlers
        register_handlers()
