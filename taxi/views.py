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


class ManufacturersListView(generic.ListView):
    model = Manufacturer
    paginate_by = 2


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.all().select_related("manufacturer")


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")


class DriverDetailView(generic.DetailView):
    model = Driver
