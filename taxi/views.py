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
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    queryset = Manufacturer.objects.all().select_related()
    paginate_by = 2


class CarListView(generic.ListView):
    model = Car
    paginate_by = 10
    queryset = Car.objects.all().select_related()
    template_name = "taxi/car-list.html"
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car
    template_name = "taxi/car-detail.html"


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 3
    template_name = "taxi/driver-list.html"


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related()
    template_name = "taxi/driver-detail.html"
