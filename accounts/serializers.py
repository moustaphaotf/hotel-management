from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=True)
    accepted_terms = serializers.BooleanField(write_only=True, required=True)


    class Meta:

        model = User
        fields = ["id", "name", "email", "password", "accepted_terms"]
        extra_kwargs = {"password": {"write_only": True}, "email": {"required": True}, "username": {"required": False}}

    
    def validate_accepted_terms(self, value):
        if not value:
            raise serializers.ValidationError("Vous devez accepter les conditions d'utilisation")

    def validate_email(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Un utilisateur avec cet email existe déjà.")
        return value


    
    def create(self, validated_data):
        name = validated_data.pop("name")
        validated_data.pop("accepted_terms")
        if User.objects.filter(email=validated_data["email"]).exists():
            raise serializers.ValidationError("Un utilisateur avec cet email existe déjà.")
        
        user = User.objects.create_user(
            username=validated_data["email"],
            first_name=name,
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "email"]