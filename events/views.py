from rest_framework import generics, permissions
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer, RegistrationCreateSerializer
from rest_framework.response import Response
from rest_framework import status


class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    

class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    
class RegistrationCreateView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class MyRegistrationsView(generics.ListAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)


class RegistrationDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    
