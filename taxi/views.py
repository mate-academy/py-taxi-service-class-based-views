from django.shortcuts import render
from django.views.generic import ListView, DetailView

from taxi.models import Car, Driver, Manufacturer


class ManufacturerListView(ListView):
    model = Manufacturer
    paginate_by = 5
    queryset = Manufacturer.objects.order_by("name")


class CarListView(ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer").order_by("model")


class CarDetailView(DetailView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")


class DriverListView(ListView):
    model = Driver
    paginate_by = 5
    queryset = Driver.objects.order_by("username")


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)
