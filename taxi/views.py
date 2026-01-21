from django.shortcuts import render
from django.views.generic import DetailView, ListView

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
    queryset = Manufacturer.objects.all().order_by("name")
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 5


class CarListView(ListView):
    queryset = Car.objects.select_related("manufacturer")
    context_object_name = "car_list"
    template_name = "taxi/car_list.html"
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    context_object_name = "driver_list"
    paginate_by = 5


class DriverDetailView(DetailView):
    queryset = Driver.objects.prefetch_related("cars")
    context_object_name = "driver"
