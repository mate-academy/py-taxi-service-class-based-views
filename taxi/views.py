from django.http import HttpResponse, HttpRequest
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
    queryset = (Manufacturer.objects.order_by("name"))
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5
    template_name = "taxi/car_list.html"


class CarDetailView(generic.DetailView):
    model = Car
    template_name = "taxi/car_detail.html"
    context_object_name = "car"
    pk_url_kwarg = "pk"


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    ordering = ["username"]
    template_name = "taxi/driver_list.html"


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver"
    pk_url_kwarg = "pk"
