from django.shortcuts import render
from django.views import generic

from .models import Driver, Car, Manufacturer

__all__ = [
    "index",
    "ManufacturerListView",
    "CarListView",
    "CarDetailView",
    "DriverListView",
    "DriverDetailView"
]


def index(request):
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by('name')
    template_name = 'taxi/manufacturer_list.html'
    context_object_name = 'manufacturers'
    paginate_by = 2


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.all().select_related('manufacturer')
    paginate_by = 2


class CarDetailView(generic.DetailView):
    model = Car
    queryset = Car.objects.all().select_related('manufacturer').prefetch_related('drivers')


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 2


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related('cars')
    paginate_by = 2
