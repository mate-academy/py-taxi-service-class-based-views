from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Driver, Car, Manufacturer


def index(request):
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


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 2


class CarListView(ListView):
    model = Car
    queryset = Car.objects.all().select_related("manufacturer")


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    queryset = Driver.objects.all().order_by("license_number").prefetch_related("cars__drivers")
    paginate_by = 2


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__drivers")
