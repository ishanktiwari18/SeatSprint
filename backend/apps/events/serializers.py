from rest_framework import serializers
from .models import Event, Show, PriceCategory, ShowSeat

class PriceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceCategory
        fields = ['id', 'name', 'price']

class ShowSeatSerializer(serializers.ModelSerializer):
    seat_label = serializers.CharField(source='seat.seat_number')
    row_label = serializers.CharField(source='seat.row.row_label')
    section_name = serializers.CharField(source='seat.row.section.name')
    class Meta:
        model = ShowSeat
        fields = ['id', 'seat_label', 'row_label', 'section_name', 'status', 'price_category']

class ShowSerializer(serializers.ModelSerializer):
    price_categories = PriceCategorySerializer(many=True, required=False)
    class Meta:
        model = Show
        fields = ['id', 'event', 'venue', 'start_time', 'end_time', 'doors_open', 'is_cancelled', 'price_categories']

class EventSerializer(serializers.ModelSerializer):
    shows = ShowSerializer(many=True, read_only=True)
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'event_type', 'organiser', 'poster_url', 'is_active', 'shows']

class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_type', 'poster_url']
