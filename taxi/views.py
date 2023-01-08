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
    """Class for viewing the list of manufacturers on the site"""

    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"
    paginate_by = 5


class CarListView(ListView):
    """Class for viewing the list of cars on the site"""

    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class DriverListView(ListView):
    """Class for viewing the list of drivers on the site"""

    model = Driver
    paginate_by = 5


class CarDetailView(DetailView):
    """Information about car"""

    model = Car


class DriverDetailView(DetailView):
    """Information about driver"""

    model = Driver
    queryset = Driver.objects.prefetch_related("cars")
