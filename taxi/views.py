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
    template_name = "taxi/manufacturers_list.html"
    context_object_name = "manufacturers"
    pagination_by = 5


class CarListView(generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    paginate_by = 5
    queryset = Car.objects.all().select_related("manufacturer")
    context_object_name = "cars"


class CarDetailView(generic.DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(generic.ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    paginate_by = 5
    context_object_name = "drivers"


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
