from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from taxi.models import Driver, Car, Manufacturer


class CarDetailView(generic.DetailView):
    model = Car


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars", "cars__manufacturer")


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)
