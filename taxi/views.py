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
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 5
    queryset = model.objects.all()
    ordering = ["name"]


class CarListView(generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    paginate_by = 5
    queryset = model.objects.select_related("manufacturer")


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = model.objects.prefetch_related("cars")
