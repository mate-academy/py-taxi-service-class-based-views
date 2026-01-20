from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from taxi.models import Driver, Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5
    context_object_name = "manufacturer_list"


class CarListView(ListView):
    model = Car
    queryset = Car.objects.all().select_related("manufacturer")
    paginate_by = 5
    context_object_name = "car_list"


class CarDetailView(DetailView):
    model = Car
    context_object_name = "car"


class DriverListView(ListView):
    model = Driver
    paginate_by = 5
    context_object_name = "driver_list"


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars")
    context_object_name = "driver"
