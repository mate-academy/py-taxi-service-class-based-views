from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from taxi.models import Car, Driver, Manufacturer


# Create your views here.
def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    return HttpResponse(
        render(
            request,
            "taxi/index.html",
            {
                "num_drivers": num_drivers,
                "num_manufacturers": num_manufacturers,
                "num_cars": num_cars,
            },
        )
    )


class ManufacturerListView(LoginRequiredMixin, ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(LoginRequiredMixin, ListView):
    model = Car
    context_object_name = "car_list"
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    context_object_name = "car"


class DriverListView(LoginRequiredMixin, ListView):
    model = Driver
    context_object_name = "driver_list"
    paginate_by = 5


class DriverDetailView(LoginRequiredMixin, DetailView):
    model = Driver
    context_object_name = "driver"

    def get_queryset(self):
        return Driver.objects.prefetch_related("cars__manufacturer")
