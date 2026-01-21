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
    context_object_name = "manufacturer_list"
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"


class CarsListView(generic.ListView):
    model = Car
    queryset = Car.objects.all().select_related("manufacturer")
    context_object_name = "car_list"
    paginate_by = 5
    template_name = "taxi/car_list.html"


class CarDetailView(generic.DetailView):
    model = Car
    context_object_name = "car"
    template_name = "taxi/car_detail.html"


class DriversListView(generic.ListView):
    model = Driver
    context_object_name = "driver_list"
    paginate_by = 5
    template_name = "taxi/driver_list.html"


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars")
    context_object_name = "driver"
    template_name = "taxi/driver_detail.html"
