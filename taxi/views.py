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
    queryset = Manufacturer.objects.order_by("name")
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 2


class CarListView(ListView):
    model = Car
    paginate_by = 2
    queryset = Car.objects.select_related("manufacturer")


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    paginate_by = 2


class DriverDetailView(DetailView):
    model = Driver
    paginate_by = 2
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
