from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    image = serializers.ImageField(required=False)

    class Meta:
        model = Hotel
        fields = [
            "id",
            "owner",
            "name",
            "address",
            "email",
            "phone",
            "price_per_night",
            "currency",
            "image",
            "created_at",
            "updated_at",
        ]