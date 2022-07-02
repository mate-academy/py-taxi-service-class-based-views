from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name", "country"]

    def __str__(self):
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    licence_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def get_absolute_url(self):
        return reverse("taxi:driver_detail", args=[str(self.id)])


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name="cars")

    class Meta:
        ordering = ["manufacturer", "model"]

    def __str__(self):
        return f"{self.manufacturer.name} {self.model}"

    def get_absolute_url(self):
        return reverse("taxi:car_detail", args=[str(self.id)])
