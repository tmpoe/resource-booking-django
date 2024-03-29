from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from resource_booking.booking import views as booking_views
from users import views as user_views

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'groups', user_views.GroupViewSet)
router.register(r'bookings', booking_views.BookingViewSet)
router.register(r'rooms', booking_views.RoomViewSet)
router.register(r'sites', booking_views.SiteViewSet)


urlpatterns = [
    path("booking/", include("booking.urls")),
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
]