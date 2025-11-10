from django.shortcuts import render
from .models import Hotel
from .serializers import HotelSerializer
from rest_framework import viewsets, permissions


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.filter(is_active=True)
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)