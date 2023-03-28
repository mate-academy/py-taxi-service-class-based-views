from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("taxi:manufacturer-detail", args=[str(self.id)])


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return self.license_number

    def get_absolute_url(self):
        return reverse("taxi:driver-detail", args=[str(self.id)])


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )
    drivers = models.ManyToManyField(Driver)

    class Meta:
        default_related_name = "cars"

    def __str__(self) -> str:
        return self.model

    def get_absolute_url(self):
        return reverse("taxi:car-detail", args=[str(self.id)])
