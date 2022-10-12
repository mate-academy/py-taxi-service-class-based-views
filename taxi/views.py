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
    """View the manufacturer's page"""

    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    """View all car`s"""

    model = Car
    queryset = Car.objects.all().select_related("manufacturer")
    paginate_by = 5


class CarDetailView(generic.DetailView):
    """View all car details"""

    model = Car


class DriverListView(generic.ListView):
    """View  all driver`s"""

    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    """View info about all drivers"""

    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")
