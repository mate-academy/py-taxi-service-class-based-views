
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

    return render(request, "taxi/index.html",
                  context=context)


class ManufacturerListViews(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListViews(generic.ListView):
    model = Car
    queryset = Car.objects.all().select_related("manufacturer")
    paginate_by = 5


class DriverListViews(generic.ListView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars")
    paginate_by = 5


def car_detail_view(request, pk):
    car = Car.objects.get(pk=pk)
    context = {"car": car}
    return render(request, "taxi/car_detail.html",
                  context=context)


def driver_detail_view(request, pk):
    driver = Driver.objects.get(id=pk)
    context = {"driver": driver}
    return render(request, "taxi/driver_detail.html",
                  context=context)
