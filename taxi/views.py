from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404

from taxi.models import Driver, Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
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
    context_object_name = "manufacturer_list"
    ordering = ["name", ]
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class DriversListView(ListView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars")
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car


class DriversDetailView(DetailView):
    model = Driver
