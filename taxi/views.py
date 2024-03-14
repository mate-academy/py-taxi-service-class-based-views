from django.shortcuts import render
from django.views.generic import ListView, DetailView

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    ordering = ("name",)
    context_object_name = "manufacturer"
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    ordering = ("model",)
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class DriverListView(ListView):
    model = Driver
    ordering = ("username",)
    context_object_name = "drivers"
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    context_object_name = "driver"
