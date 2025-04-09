from rest_framework import serializers
from .models import Event, Registration
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "date",
            "location",
        ]
        
        
class RegistrationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ["user","event"]
    
    
    
class RegistrationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    event_title = serializers.CharField(source='event.title', read_only=True)
    registered_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S', read_only=True)
    class Meta:
        model = Registration
        fields = [
            "id",
            "user",
            "event_title",
            "registered_at",
        ]
    