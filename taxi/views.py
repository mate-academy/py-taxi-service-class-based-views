from django.shortcuts import render
from django.views.generic import ListView, DetailView

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    return render(request,
                  "taxi/index.html", {
                      "num_drivers": Driver.objects.count(),
                      "num_cars": Car.objects.count(),
                      "num_manufacturers": Manufacturer.objects.count(), }
                  )


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    template_name = "taxi/car_list.html"
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer")


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
