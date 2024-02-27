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
    paginate_by = 5

    def get_queryset(self):
        return Manufacturer.objects.order_by("name")


class CarListView(generic.ListView):
    model = Car
    paginate_by = 5

    def get_queryset(self):
        return Car.objects.select_related("manufacturer")


class CarDetailView(generic.DetailView):
    model = Car

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related("drivers")
        return queryset


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver

    def get_queryset(self):
        return Driver.objects.prefetch_related("cars__manufacturer")
