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


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    paginate_by = 5
    ordering = ["name"]


class CarsListView(generic.ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.all().select_related("manufacturer")


class DriversListView(generic.ListView):
    model = Driver
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car

    def get_queryset(self):
        return Car.objects.filter(
            pk=self.kwargs.get("pk")
        ).prefetch_related("drivers").select_related("manufacturer")


class DriverDetailView(generic.DetailView):
    model = Driver

    def get_object(self, queryset=None):
        return Driver.objects.filter(
            pk=self.kwargs.get("pk")
        ).prefetch_related("cars__manufacturer")
