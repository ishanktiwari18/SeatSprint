from django.urls import re_path
from .consumers import SeatStatusConsumer

websocket_urlpatterns = [
    re_path(r'ws/shows/(?P<show_id>[0-9a-f-]+)/seats/$', SeatStatusConsumer.as_asgi()),
]
