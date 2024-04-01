from django.urls import include, path

from rest_framework import routers

from users import views as user_views

router = routers.DefaultRouter()

router.register(r'users', user_views.UserViewSet, basename='user')
router.register(r'groups', user_views.GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
]