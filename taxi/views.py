from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView

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
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5


class CarsListView(generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"
    paginate_by = 5
    queryset = Car.objects.\
        select_related("manufacturer").\
        prefetch_related("drivers").order_by("drivers").all()


def car_detail_view(request, pk):
    car = Car.objects.get(pk=pk)

    context = {
        "car": car
    }
    return render(request, "taxi/car_detail.html", context=context)


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    template_name = "taxi/driver_list.html"


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    queryset = Driver.objects.all().prefetch_related("cars")
