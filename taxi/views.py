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
    context_object_name = "manufacturer_list"
    paginate_by = 5
    queryset = Manufacturer.objects.order_by("name")


class CarListView(generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"
    paginate_by = 5
    queryset = Car.objects.select_related(
        "manufacturer"
    ).prefetch_related("drivers")


class CarDetailView(generic.DetailView):
    model = Car
    # context_object_name = "car_detail"
    template_name = "taxi/car_detail.html"


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    context_object_name = "driver_list"
    template_name = "taxi/driver_list.html"


class DriverDetailView(generic.DetailView):
    model = Driver
    # context_object_name = "driver_detail"
    queryset = Driver.objects.prefetch_related("cars")
    template_name = "taxi/driver_detail.html"
