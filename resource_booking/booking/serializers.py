from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Booking, Room, Site


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
        
class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['room', 'start_time', 'end_time', 'user']
        

class RoomSerializer(serializers.HyperlinkedModelSerializer):  
    
    class Meta:
        model = Room
        fields = ['name', 'site', 'size']
        

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ['name']