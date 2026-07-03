from rest_framework import serializers
from .models import WaitlistEntry

class WaitlistJoinSerializer(serializers.Serializer):
    show_id = serializers.UUIDField()
    requested_seats = serializers.IntegerField(min_value=1, default=1)

class WaitlistEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitlistEntry
        fields = ['id','show','position','requested_seats','status','offer_expires_at','created_at']
