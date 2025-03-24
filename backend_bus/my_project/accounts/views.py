# accounts/views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer

# Register API View
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login API View
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is not None:
            # If authenticated, return all user details
            user_data = {
                "username": user.username,
                "email": user.email,
                "userType": user.userType,
                "phoneNumber": user.phoneNumber,
                "department": user.department,
                "address": user.address,
                "user_Number": user.user_Number,
            }
            return Response(user_data, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
