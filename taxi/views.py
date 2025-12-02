from django.views import generic
from .models import Manufacturer, Car, Driver

class ManufacturerListView(generic.ListView):
    model = Manufacturer
    paginate_by = 5
    ordering = ["name"]
    template_name = "taxi/manufacturer_list.html"

class CarListView(generic.ListView):
    model = Car
    paginate_by = 5
    template_name = "taxi/car_list.html"

    def get_queryset(self):
        return Car.objects.select_related("manufacturer")

class CarDetailView(generic.DetailView):
    model = Car
    template_name = "taxi/car_detail.html"

class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    template_name = "taxi/driver_list.html"

class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"

    def get_queryset(self):
        return Driver.objects.prefetch_related("cars__manufacturer")
