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
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5

    # The README says: Set the appropriate context variable name,
    # that you will use in the template.

    # But it looks like the names I'd want to assign are default anyway.
    # context_object_name = "manufacturer_list"
    # template_name = "taxi/manufacturer_list.html"


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car
    queryset = Car.objects.select_related("manufacturer").prefetch_related(
        "drivers"
    )


class DriverListView(ListView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars")
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
