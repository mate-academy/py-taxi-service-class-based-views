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
    template_name = "taxi/manufacturer_list.html"
    queryset = Manufacturer.objects.order_by("name")
    ordering = "name"
    paginate_by = 5


class CarListView(ListView):
    model = Car
    template_name = "taxi/car_list.html"
    queryset = Car.objects\
        .select_related("manufacturer")\
        .prefetch_related("drivers")
    ordering = "model"
    paginate_by = 5


class DriverListView(ListView):
    model = Driver
    ordering = "username"
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars")
