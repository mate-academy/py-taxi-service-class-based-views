from django.shortcuts import render
from django.views.generic import ListView, DetailView
from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""
    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }
    return render(request, "taxi/index.html", context)


class ManufacturerListView(ListView):
    model = Manufacturer
    paginate_by = 5
    context_object_name = "manufacturer_list"
    queryset = Manufacturer.objects.all()


class CarListView(ListView):
    model = Car
    paginate_by = 5
    context_object_name = "car_list"
    queryset = Car.objects.select_related("manufacturer")


class CarDetailView(DetailView):
    model = Car
    context_object_name = "car"


class DriverListView(ListView):
    model = Driver
    paginate_by = 5
    context_object_name = "driver_list"


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
    context_object_name = "driver"
