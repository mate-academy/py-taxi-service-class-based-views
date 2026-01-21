from tkinter.font import names

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.views import generic


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(Driver, related_name="cars")


class ManufacturerListView(generic.ListView):
    paginate_by = 5

    def get_queryset(self):
        return Manufacturer.objects.all().order_by("name")
