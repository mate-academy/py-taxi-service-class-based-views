from django.views.generic import ListView, DetailView

from .models import Manufacturer, Car, Driver


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"
    paginate_by = 5

    def get_queryset(self):
        return Manufacturer.objects.order_by("name")


class CarListView(ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"
    paginate_by = 5

    def get_queryset(self):
        return Car.objects.select_related("manufacturer").order_by("id")


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"
    paginate_by = 5

    def get_queryset(self):
        return Driver.objects.order_by("id")


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
