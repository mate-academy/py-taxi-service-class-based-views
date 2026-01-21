from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}. Located in {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse("taxi:driver-detail", args=[str(self.id)])


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    def get_absolute_url(self):
        return reverse("taxi:car-detail", args=[str(self.id)])
