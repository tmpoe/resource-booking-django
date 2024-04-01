from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import permissions, viewsets, views, authentication

from booking.serializers import BookingSerializer, RoomSerializer, SiteSerializer
from booking.models import Booking, Room, Site

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

    
    
class BookingViewSet(views.APIView):
    """
    API endpoint that allows bookings to be viewed or edited.
    """
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = BookingSerializer
    queryset = Room.objects.all()
    basename = 'booking'
    
    def get(self, request, format=None):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True,  context={'request': request})
        return Response(serializer.data)
    
    
class RoomViewSet(views.APIView):
    """
    API endpoint that allows rooms to be viewed or edited.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True, context={'request': request})
        print(serializer.data)
        return Response(serializer.data)
    
    
class SiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sites to be viewed or edited.
    """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAuthenticated]