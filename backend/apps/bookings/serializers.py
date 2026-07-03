from rest_framework import serializers
from .models import Booking, BookingItem

class BookingItemSerializer(serializers.ModelSerializer):
    seat_label = serializers.CharField(source='show_seat.seat.seat_number', read_only=True)
    row_label = serializers.CharField(source='show_seat.seat.row.row_label', read_only=True)
    section = serializers.CharField(source='show_seat.seat.row.section.name', read_only=True)
    class Meta:
        model = BookingItem
        fields = ['id','show_seat','seat_label','row_label','section','price']

class BookingSerializer(serializers.ModelSerializer):
    items = BookingItemSerializer(many=True, read_only=True)
    show_title = serializers.CharField(source='show.event.title', read_only=True)
    show_time = serializers.DateTimeField(source='show.start_time', read_only=True)
    venue_name = serializers.CharField(source='show.venue.name', read_only=True)
    class Meta:
        model = Booking
        fields = ['id','booking_number','user','show_title','show_time','venue_name','status','total_amount','items','created_at','booked_at','cancelled_at','cancellation_reason','qr_code_url']
        read_only_fields = ['booking_number','status','total_amount','booked_at','qr_code_url']

class BookingInitiateSerializer(serializers.Serializer):
    show_id = serializers.UUIDField()
    seat_ids = serializers.ListField(child=serializers.UUIDField())

class BookingCancelSerializer(serializers.Serializer):
    reason = serializers.CharField(required=False, allow_blank=True)
