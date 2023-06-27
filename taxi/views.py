from django.shortcuts import render
from django.views.generic import DetailView, ListView

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
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"
    queryset = Manufacturer.objects.all().order_by("name")


class CarListView(ListView):
    model = Car
    context_object_name = "car_list"
    paginate_by = 5
    template_name = "taxi/car_list.html"
    queryset = (
        Car.objects.all().select_related("manufacturer").
        prefetch_related("drivers")
    )


class CarDetailView(DetailView):
    model = Car
    queryset = (
        Car.objects.all().select_related("manufacturer").
        prefetch_related("drivers")
    )


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars")
