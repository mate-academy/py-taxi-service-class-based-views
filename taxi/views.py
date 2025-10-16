from django.shortcuts import render
from django.views.generic import ListView, DetailView

from taxi.models import Driver, Car, Manufacturer


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    template_name = "taxi/car_list.html"
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car
    queryset = (Car.objects
                .select_related("manufacturer")
                .prefetch_related("drivers")
                )
    template_name = "taxi/car_detail.html"


class DriverListView(ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
    template_name = "taxi/driver_detail.html"


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)
