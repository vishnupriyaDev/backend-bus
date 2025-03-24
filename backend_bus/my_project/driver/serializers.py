from rest_framework import serializers
from .models import Bus, Driver

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'name', 'route']

class DriverSerializer(serializers.ModelSerializer):
    bus = BusSerializer()

    class Meta:
        model = Driver
        fields = ['id', 'name', 'license_number', 'phone_number', 'bus']
