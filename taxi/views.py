from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    paginate_by = 5
    queryset = Manufacturer.objects.order_by("name")


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5

    def get_queryset(self):
        return Driver.objects.all().order_by("license_number")


class CarDetailView(generic.DetailView):
    model = Car


class CarListView(generic.ListView):
    model = Car
    paginate_by = 5

    def get_queryset(self):
        return Car.objects.order_by("model")


class DriverDetailView(generic.DetailView):
    model = Driver

    def get_queryset(self):
        return Driver.objects.order_by("cars")
