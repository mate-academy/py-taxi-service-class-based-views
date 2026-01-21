from django.shortcuts import render
from django.views.generic import ListView, DetailView

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    return render(
        request,
        "taxi/index.html",
        context={
            "num_drivers": Driver.objects.count(),
            "num_cars": Car.objects.count(),
            "num_manufacturers": Manufacturer.objects.count(),
        })


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = (Car.objects.all().order_by("model")
                .select_related("manufacturer"))
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["drivers"] = self.object.drivers.all()
        return context


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = self.object.cars.all()
        return context
