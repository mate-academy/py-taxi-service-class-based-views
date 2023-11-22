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
    queryset = Manufacturer.objects.prefetch_related("cars").order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.prefetch_related("manufacturer", "drivers")
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car
    queryset = Car.objects.prefetch_related("manufacturer", "drivers")


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    queryset = Driver.objects.prefetch_related("cars")


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars", "cars__manufacturer")
