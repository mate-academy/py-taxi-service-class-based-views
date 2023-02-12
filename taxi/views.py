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
    queryset = Manufacturer.objects.order_by("name")
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer").order_by("model")
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car
    queryset = Car.objects.select_related("manufacturer").order_by("model")


class DriverListView(generic.ListView):
    moder = Driver
    paginate_by = 5
    queryset = Driver.objects.prefetch_related(
        "cars__manufacturer"
    ).order_by("first_name")


class DriverDetailView(generic.DetailView):
    model = Driver
