from rest_framework import serializers
from .models import Venue, Section, Row, Seat

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'seat_type', 'is_available']

class RowSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, required=False)
    class Meta:
        model = Row
        fields = ['id', 'row_label', 'seats']

class SectionSerializer(serializers.ModelSerializer):
    rows = RowSerializer(many=True, required=False)
    class Meta:
        model = Section
        fields = ['id', 'name', 'rows']

class VenueCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    zip_code = serializers.CharField()
    sections = SectionSerializer(many=True, write_only=True)

class VenueSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
    class Meta:
        model = Venue
        fields = ['id', 'name', 'address', 'city', 'state', 'zip_code', 'total_capacity', 'sections']
