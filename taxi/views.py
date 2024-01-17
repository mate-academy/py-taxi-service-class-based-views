from typing import Any
from django.contrib.auth import get_user_model
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from taxi.models import Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": get_user_model().objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = get_user_model()
    paginate_by = 5


class DriverDetailView(DetailView):
    model = get_user_model()
    queryset = get_user_model().objects.prefetch_related("cars__manufacturer")
