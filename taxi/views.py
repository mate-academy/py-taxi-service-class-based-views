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
    """Generic class-based view for a list of manufacturers."""

    model = Manufacturer
    context_object_name = "manufacturer_list"
    queryset = Manufacturer.objects.all()
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 2


class CarListView(generic.ListView):
    """Generic class-based view for a list of cars."""

    model = Car
    queryset = Car.objects.all().select_related("manufacturer")
    paginate_by = 2


class CarDetailView(generic.DetailView):
    """Generic class-based detail view for a car."""

    model = Car


class DriverListView(generic.ListView):
    """Generic class-based view for a list of drivers."""

    model = Driver
    paginate_by = 2


class DriverDetailView(generic.DetailView):
    """Generic class-based detail view for a driver."""

    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")
