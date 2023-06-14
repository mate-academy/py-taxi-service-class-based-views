from typing import Callable

from django.shortcuts import render
from django.views import generic

from .models import Driver, Car, Manufacturer


def index(request) -> Callable:
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.all().select_related("manufacturer")


class CarDetailView(generic.DetailView):
    model = Car
    queryset = Car.objects.all().select_related(
        "manufacturer"
    ).prefetch_related("drivers")


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars")
