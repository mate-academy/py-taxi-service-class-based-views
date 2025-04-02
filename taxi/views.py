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

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class ManufacturerDetailView(DetailView):
    model = Manufacturer


class CarListView(ListView):
    model = Car
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car

    def get_queryset(self):
        return (
            super().get_queryset()
                   .select_related("manufacturer")
                   .prefetch_related("drivers")
        )


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver

    def get_queryset(self):
        return (
            super().get_queryset()
                   .prefetch_related("cars")
        )
