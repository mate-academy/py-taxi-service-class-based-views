from django.db.models import Prefetch
from django.shortcuts import render
from django.views import generic

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num-drivers": Driver.objects.count(),
        "num-cars": Car.objects.count(),
        "num-manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    paginate_by = 5
    ordering = "name"


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    ordering = ["id"]
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    ordering = ["username"]
    paginate_by = 5


def grt_queryset():
    return Driver.objects.all().prefetch_related(
        Prefetch(
            "cars",
            queryset=Car.objects.select_related("manufacturer"),
        )
    )


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver"
