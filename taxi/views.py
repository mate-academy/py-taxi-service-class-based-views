from django.shortcuts import render
from django.views import generic

from .models import Driver, Car, Manufacturer


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    context_object_name = "car_list"
    template_name = "taxi/car_list.html"
    paginate_by = 5
    # Optimization: select_related for ForeignKey (Manufacturer)
    queryset = Car.objects.select_related("manufacturer")


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    context_object_name = "driver_list"
    template_name = "taxi/driver_list.html"
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    # Optimization: prefetch_related for M2M (cars) and select_related
    # for the nested ForeignKey (manufacturer of those cars)
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
