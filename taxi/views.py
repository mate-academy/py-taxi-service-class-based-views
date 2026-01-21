from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from taxi.models import Driver, Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""
    print(request)
    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all()
    paginate_by = 5
    context_object_name = "manufacturer_list"


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer").all()
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
    queryset = Driver.objects.prefetch_related("cars").all()
    context_object_name = "driver"
