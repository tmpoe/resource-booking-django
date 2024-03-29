from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from booking import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'bookings', views.BookingViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'sites', views.SiteViewSet)


urlpatterns = [
    path("booking/", include("booking.urls")),
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
]