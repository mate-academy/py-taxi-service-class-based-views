from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.all().select_related("manufacturer")


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        context["cars"] = Car.objects.select_related("manufacturer").filter(
            drivers__id=pk
        )
        return context
