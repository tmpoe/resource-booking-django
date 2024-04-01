from django.urls import include, re_path, path

from booking import views

from rest_framework import routers

from booking import views


router = routers.DefaultRouter()
router.register(r'sites', views.SiteViewSet, basename='site')
router.register(r'bookings/(?P<room_name>.+)', views.BookingViewSet, basename='booking')
router.register(r'rooms/(?P<site_name>.+)/(?P<room_name>.+)', views.RoomViewSet, basename='room2')
router.register(r'room', views.RoomViewSet, basename='room')


urlpatterns = [
    path('', views.index, name="index"),
    path('', include(router.urls)),
]