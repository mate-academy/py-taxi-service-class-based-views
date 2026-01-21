from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView (generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"


class CarListView (generic.ListView):
    model = Car
    paginate_by = 5
    template_name = "taxi/car_list.html"
    queryset = Car.objects.select_related("manufacturer").all()


class CarDetailView (generic.DetailView):
    model = Car
    context_object_name = "car"
    template_name = "taxi/car_detail.html"


class DriverListView (generic.ListView):
    model = Driver
    paginate_by = 5
    template_name = "taxi/driver_list.html"
    queryset = Driver.objects.all()


class DriverDetailView (generic.DetailView):
    model = Driver
    context_object_name = "driver"
    template_name = "taxi/driver_detail.html"
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
