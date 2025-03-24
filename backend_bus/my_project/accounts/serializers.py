# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'userType', 'phoneNumber', 'department', 'address', 'user_Number']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            userType=validated_data['userType'],
            phoneNumber=validated_data['phoneNumber'],
            department=validated_data['department'],
            address=validated_data['address'],
            user_Number=validated_data['user_Number']
        )
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'userType', 'phoneNumber', 'department', 'address', 'user_Number']
