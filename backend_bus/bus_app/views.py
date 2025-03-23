from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.serializers import Serializer, CharField

# Serializer for Register
class RegisterSerializer(Serializer):
    username = CharField(max_length=100)
    password = CharField(write_only=True, style={'input_type': 'password'})
    email = CharField(max_length=100)

# Register API View
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            email = serializer.validated_data['email']

            # Check if username already exists
            if User.objects.filter(username=username).exists():
                return Response({"detail": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

            # Create user
            user = User.objects.create_user(username=username, password=password, email=email)
            return Response({"detail": "User created successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Custom TokenObtainPairView to include a refresh token
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response

# Token Refresh View
class TokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]
