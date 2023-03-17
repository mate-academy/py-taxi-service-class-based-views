from django.shortcuts import render
from django.views.generic import ListView, DetailView

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


class ManufacturerListView(ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 5
    ordering = "name"


class CarListView(ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.all().select_related("manufacturer")
    # template_name = "taxi/car_list.html"


class CarDetailView(DetailView):
    model = Car
    # template_name = "taxi/car_detail.html"


class DriverListView(ListView):
    model = Driver
    paginate_by = 5
    # template_name = "taxi/driver_list.html"


class DriverDetailView(DetailView):
    model = Driver
    # template_name = "taxi/driver_detail.html"
