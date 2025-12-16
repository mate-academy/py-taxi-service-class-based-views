from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Manufacturer, Driver, Car
from django.contrib.auth import get_user_model


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
    queryset = Manufacturer.objects.all().order_by("name")
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        print("ManufacturerListView accessed")
        return super().get(request, *args, **kwargs)


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer").all()
    template_name = "taxi/car_list.html"
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(ListView):
    model = get_user_model()
    template_name = "taxi/driver_list.html"
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("cars__manufacturer")
