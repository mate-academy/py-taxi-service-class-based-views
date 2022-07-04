from django.shortcuts import render
from django.views import generic

from .models import Driver, Car, Manufacturer


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
    context_object_name = "manufacturer_list"
    paginate_by = 1
    queryset = Manufacturer.objects.order_by("name")


class CarsListView(generic.ListView):
    model = Car


class CarsDetailedListView(generic.DetailView):
    model = Car


class DriversListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriversDetailedListView(generic.DetailView):
    model = Driver
    queryset = Car.objects.select_related("manufacturer")