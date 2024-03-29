from django.contrib import admin

from .models import Booking, Room, Site

# Register your models here.
admin.site.register(Site)
admin.site.register(Room)
admin.site.register(Booking)