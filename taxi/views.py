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
    context_object_name = "manufacturers"
    queryset = Manufacturer.objects.all()
    paginate_by = 2
    template_name = "taxi/manufacturer_list.html"


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    context_object_name = "cars"
    paginate_by = 3
    template_name = "taxi/car_list.html"


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"
    queryset = Car.objects.prefetch_related("drivers").select_related("manufacturer")


class DriverListView(ListView):
    model = Driver
    paginate_by = 4
    template_name = "taxi/driver_list.html"
    context_object_name = "drivers"


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver"
    queryset = Driver.objects.prefetch_related()
