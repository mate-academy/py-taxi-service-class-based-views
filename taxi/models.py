from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse("taxi:driver-detail", args=[str(self.id)])

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
        ordering = ["username"]


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name="cars")

    def get_absolute_url(self):
        return reverse("taxi:car-detail", args=[str(self.id)])

    class Meta:
        ordering = ["model"]
