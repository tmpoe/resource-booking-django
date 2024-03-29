from django.urls import path

from . import booking_views

urlpatterns = [
    path("", booking_views.index, name="index"),
]