from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpRequest, HttpResponse

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
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer").order_by("id")
    context_object_name = "car_list"
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"
    context_object_name = "car"


class DriverListView(ListView):
    model = Driver
    queryset = Driver.objects.order_by("id")
    context_object_name = "driver_list"
    template_name = "taxi/driver_list.html"
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver"

    def get_queryset(self):
        return Driver.objects.prefetch_related(
            "cars__manufacturer"
        )
