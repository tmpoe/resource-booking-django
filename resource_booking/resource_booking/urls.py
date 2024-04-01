from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("booking/", include("booking.urls")),
    path("admin/", admin.site.urls),
]