from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

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
    template_name = "taxi/manufacturers_list.html"
    context_object_name = "manufacturers_list"
    paginate_by = 5


class CarListView(ListView):
    model = Car
    template_name = "taxi/cars_list.html"
    context_object_name = "cars_list"
    paginate_by = 5


class DriverListView(ListView):
    model = Driver
    template_name = "taxi/drivers_list.html"
    context_object_name = "drivers_list"
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/cars_detail.html"
    context_object_name = "cars_detail"


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "drivers_detail"
