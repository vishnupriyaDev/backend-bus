from django.db import models

class Bus(models.Model):
    name = models.CharField(max_length=100)
    route = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.route}"

class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    bus = models.ForeignKey(Bus, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
