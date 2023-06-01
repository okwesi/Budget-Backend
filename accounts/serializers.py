from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from .models import User


class UserCreateSerializer(BaseUserCreateSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ["id", "email", "password", "username", "password_confirmation"]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        try:
            if User.objects.filter(email=validated_data['email']).exists():
                raise serializers.ValidationError("Email already exists")
            del validated_data['password_confirmation']
            user = self.perform_create(validated_data)
        except Exception as e:
            raise serializers.ValidationError(e)

        return user
