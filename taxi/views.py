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
    paginate_by = 5
    queryset = Manufacturer.objects.order_by("name")
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"


class CarListView(ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer").order_by("model")


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    paginate_by = 5
    queryset = Driver.objects.filter(is_active=True).order_by("username")

    template_name = "taxi/driver_list.html"


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
