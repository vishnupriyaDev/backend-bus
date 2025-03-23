from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),  # Custom view to obtain token pair
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token view
]
