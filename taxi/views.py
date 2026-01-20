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
    template_name = "taxi/manufacturer_list.html"
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    context_object_name = "car_list"
    template_name = "taxi/car_list.html"
    queryset = Car.objects.select_related("manufacturer").order_by("model")
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    context_object_name = "driver_list"
    queryset = Driver.objects.prefetch_related("cars").order_by("username")
    template_name = "taxi/driver_list.html"
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars")
