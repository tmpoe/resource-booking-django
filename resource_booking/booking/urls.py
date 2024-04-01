from django.urls import include, path

from booking import views

from rest_framework import routers

from booking import views


router = routers.DefaultRouter()
router.register(r'sites', views.SiteViewSet, basename='site')

urlpatterns = [
    path('', views.index, name="index"),
    path('', include(router.urls)),
    path('api/booking', views.BookingViewSet.as_view(), name='booking'),
    path('api/room', views.RoomViewSet.as_view(), name='room'),
]