from django.urls import include, path

from booking import views

from rest_framework import routers

from booking import views as booking_views
from users import views as user_views


router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'groups', user_views.GroupViewSet)
router.register(r'rooms', booking_views.RoomViewSet)
router.register(r'sites', booking_views.SiteViewSet)
router.register(r'bookings', booking_views.BookingViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('', include(router.urls)),
    
]