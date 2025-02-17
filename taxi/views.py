from django.shortcuts import render
from django.views.generic import ListView, DetailView
from taxi.models import Driver, Car, Manufacturer
from django.db.models import Prefetch


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
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturers"
    ordering = ["name"]
    paginate_by = 5


class CarListView(ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "cars"
    paginate_by = 5
    ordering = ["id"]  # Ensures consistent pagination order

    def get_queryset(self):
        return Car.objects.select_related("manufacturer")


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "drivers"
    paginate_by = 5
    ordering = ["id"]  # Ensures consistent pagination order


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"

    def get_queryset(self):
        return Driver.objects.prefetch_related(
            Prefetch("cars",
                     queryset=Car.objects.select_related("manufacturer"))
        )
