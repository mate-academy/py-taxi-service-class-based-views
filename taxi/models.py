from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name", ]

    def __str__(self) -> str:
        return f"{self.name} - {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def get_absolute_url(self):
        return reverse("taxi:driver-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return (
            f"{self.username} "
            f"({self.first_name} {self.last_name} "
            f"{self.license_number})"
        )


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name="cars")

    def __str__(self) -> str:
        return f"{self.model}, manufacturer: {self.manufacturer.name}"

    def get_absolute_url(self):
        return reverse("taxi:car-detail", args=[str(self.id)])
