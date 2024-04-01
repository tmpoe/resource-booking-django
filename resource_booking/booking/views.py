from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import permissions, viewsets, views, authentication, generics

from booking.serializers import BookingSerializer, RoomSerializer, SiteSerializer
from booking.models import Booking, Room, Site

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

    
    
class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed or edited.
    """
    serializer_class = BookingSerializer
    
    def get_queryset(self):
        return Booking.objects.all().filter(room__name=self.kwargs["room_name"])

    
    
class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rooms to be viewed or edited.
    """
    serializer_class = RoomSerializer
    def get_queryset(self):
        return Room.objects.all().filter(name=self.kwargs["room_name"], site__name=self.kwargs["site_name"])
    
    
class SiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sites to be viewed or edited.
    """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer