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
    queryset = Manufacturer.objects.order_by('name')
    paginate_by = 5


class CarListView(ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related('manufacturer')


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related('cars__manufacturer')
