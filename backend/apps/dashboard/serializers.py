from rest_framework import serializers

class DashboardSerializer(serializers.Serializer):
    total_bookings = serializers.IntegerField()
    total_revenue = serializers.CharField()
