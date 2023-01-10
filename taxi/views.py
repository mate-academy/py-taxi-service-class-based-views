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
    queryset = Manufacturer.objects.all().order_by("name")
    template = "templates/taxi"
    context_object_name = "manufacturer_list"
    paginate_by = 5


class CarListView(generic.ListView):
    queryset = Car.objects.all().select_related("manufacturer")
    paginate_by = 5


class CarDetailView(generic.DetailView):
    queryset = Car.objects.all()


class DriverListView(generic.ListView):
    queryset = Driver.objects.all()
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    queryset = Driver.objects.all().prefetch_related("cars")
