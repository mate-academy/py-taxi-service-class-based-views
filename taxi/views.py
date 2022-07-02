from django.shortcuts import render
from django.views import generic
from .models import Driver, Car, Manufacturer


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    template_name = "taxi/manufacturers.html"
    context_object_name = "brands"
    paginate_by = 10


class CarListView(generic.ListView):
    model = Car
    template_name = "taxi/cars_list.html"
    context_object_name = "cars"
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 10


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    template_name = "taxi/drivers_list.html"
    context_object_name = "drivers"
    paginate_by = 10


class DriverDetailView(generic.DetailView):
    model = Driver
    paginate_by = 10
    queryset = Driver.objects.prefetch_related("cars__manufacturer")


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
