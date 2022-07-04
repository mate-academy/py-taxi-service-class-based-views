from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return str(self.name)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
        ordering = ["username"]

    def get_absolut_url(self):
        return reverse("taxi:driver-detail", args=[str(self.pk)])


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name="cars")

    def get_absolut_url(self):
        return reverse("taxi:car-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.manufacturer} {self.model}"
