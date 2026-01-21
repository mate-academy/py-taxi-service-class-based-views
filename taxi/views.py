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
    queryset = Manufacturer.objects.all()
    ordering = "name"
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars")
