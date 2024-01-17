# views.py

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


class CarListView(generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Car.objects.prefetch_related("manufacturer").order_by("id")


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    template_name = "taxi/car_list.html"
    paginate_by = 5
    ordering = ["name"]
    context_object_name = "manufacturer_list"


class CarDetailView(generic.DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(generic.ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Driver.objects.all().order_by("id")


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
