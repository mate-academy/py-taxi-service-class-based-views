from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import generic

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
    queryset = (Manufacturer.objects.order_by("name"))
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5
    template_name = "taxi/car_list.html"


def car_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    car = Car.objects.get(id=pk)
    context = {
        "car": car,
    }
    return render(request, "taxi/car_detail.html", context=context)


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    ordering = ["username"]
    template_name = "taxi/driver_list.html"


def driver_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    driver = Driver.objects.get(id=pk)
    context = {
        "driver": driver,
    }
    return render(request, "taxi/driver_detail.html", context=context)
