# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    userType = models.CharField(max_length=100, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    user_Number = models.CharField(max_length=100, blank=True, null=True)
