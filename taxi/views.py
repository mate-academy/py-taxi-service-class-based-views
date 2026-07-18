from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Prefetch

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    """View function for the home page of the site."""

    model = Manufacturer
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5


class CarListView(ListView):
    """View function for the home page of the site."""

    model = Car
    queryset = Car.objects.select_related("manufacturer").all()
    paginate_by = 5


class CarDetailView(DetailView):
    """View function for the home page of the site."""

    model = Car


class DriverListView(ListView):
    """View function for the home page of the site."""

    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    """View function for the home page of the site."""

    model = Driver
    queryset = Driver.objects.prefetch_related(
        Prefetch("cars", queryset=Car.objects.select_related("manufacturer"))
    )
