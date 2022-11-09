from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Driver, Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }

    return render(
        request=request, template_name="taxi/index.html", context=context
    )


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5
    context_object_name = "car_list"
    template_name = "taxi/car_list.html"


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    context_object_name = "driver_list"
    template_name = "taxi/driver_list.html"


class CarDetailedView(generic.DetailView):
    model = Car
    context_object_name = "car"
    template_name = "taxi/car_detail.html"


class DriverDetailedView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
    context_object_name = "driver"
    template_name = "taxi/driver_detail.html"
