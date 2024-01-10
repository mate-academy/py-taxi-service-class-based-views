from django.shortcuts import render
from django.views import generic

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturersListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all()
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver_detail"
    queryset = Driver.objects.prefetch_related("cars")
