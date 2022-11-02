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


def manufacturer_list_view(request):
    manufacturer_list = Manufacturer.objects.all()

    context = {
        "manufacturer_list": manufacturer_list,
    }
    return render(request, "taxi/manufacturer_list.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    queryset = Manufacturer.objects.all()
    paginate_by = 5


class CarListView(ListView):
    model = Car
    context_object_name = "car_list"
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    context_object_name = "driver_list"
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
