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
    """View to list all manufacturers."""

    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"
    paginate_by = 5
    queryset = Manufacturer.objects.all()
    ordering = ["name"]


class CarListView(ListView):
    """View to list all cars."""

    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer")
    ordering = ["model"]


class CarDetailView(DetailView):
    """View to display details of a car."""

    model = Car
    template_name = "taxi/car_detail.html"
    context_object_name = "car"
    queryset = (Car.objects
                .select_related("manufacturer")
                .prefetch_related("drivers"))

    def get_context_data(self, **kwargs):
        """Add manufacturer to the context."""
        context = super().get_context_data(**kwargs)
        context["manufacturer_list"] = self.object.manufacturer
        context["driver_list"] = self.object.drivers.all()
        return context


class DriverListView(ListView):
    """View to list all drivers."""

    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"
    paginate_by = 5
    queryset = Driver.objects.prefetch_related("cars")
    ordering = ["license_number"]


class DriverDetailView(DetailView):
    """View to display details of a driver."""

    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver"

    def get_context_data(self, **kwargs):
        """Add car to the context."""
        context = super().get_context_data(**kwargs)
        context["car_list"] = self.object.cars.all()
        return context
