# my_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # Include accounts app URLs
    path('api/bus/', include('bus.urls')),
    path('api/', include('driver.urls')),
]
