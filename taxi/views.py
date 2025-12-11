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
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturers"
    paginate_by = 5
    ordering = "name"


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    template_name = "taxi/car_list.html"
    context_object_name = "cars"
    paginate_by = 5


class CarsDetailView(generic.DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(generic.ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "drivers"
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    context_object_name = "driver"
    template_name = "taxi/driver_detail.html"
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
