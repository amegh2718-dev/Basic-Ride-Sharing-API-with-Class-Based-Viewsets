from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RideViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'rides', RideViewSet, basename='ride')

urlpatterns = router.urls
