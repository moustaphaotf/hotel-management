from django.urls import path, include
from rest_framework import routers
from .views import HotelViewSet


router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]