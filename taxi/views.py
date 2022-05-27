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
    queryset = Manufacturer.objects.all()
    paginate_by = 2


class CarListView(ListView):
    model = Car
    context_object_name = "car_list"
    template_name = "taxi/car_list.html"
    paginate_by = 2
    queryset = Car.objects.all().select_related("manufacturer")


class CarDetailView(DetailView):
    model = Car
    context_object_name = "car_detail"
    template_name = "taxi/car_detail.html"


class DriverListView(ListView):
    model = Driver
    context_object_name = "driver_list"
    template_name = "taxi/driver_list.html"
    paginate_by = 2


class DriverDetailView(DetailView):
    model = Driver
    context_object_name = "driver_detail"
    template_name = "taxi/driver_detail.html"
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")
