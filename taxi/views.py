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
    context_object_name = "manufacturer_list"
    # template_name = "taxi/manufacturer_list.html"
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car  # set
    context_object_name = "car_list"
    queryset = Car.objects.select_related("manufacturer").order_by("model")
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car
    context_object_name = "car"


class DriverListView(ListView):
    model = Driver
    context_object_name = "driver_list"
    paginate_by = 5
    queryset = Driver.objects.order_by("username")


class DriverDetailView(DetailView):
    model = Driver
    context_object_name = "driver"
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
