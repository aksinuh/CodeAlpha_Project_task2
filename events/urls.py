from django.urls import path
from .views import EventListView, EventDetailView, RegistrationCreateView, MyRegistrationsView, RegistrationDeleteAPIView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('register/', RegistrationCreateView.as_view(), name='event-register'),
    path('my-registrations/', MyRegistrationsView.as_view(), name='my-registrations'),
    path('delete-registration/<int:pk>/', RegistrationDeleteAPIView.as_view(), name='delete-registration'),
]