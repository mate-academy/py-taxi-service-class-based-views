from django.views.generic import ListView, DetailView
from django.db.models import Prefetch
from .models import Manufacturer, Car, Driver


class ManufacturerListView(ListView):
    model = Manufacturer
    paginate_by = 5
    ordering = ["name"]


class CarListView(ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer")


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related(
        Prefetch("cars", queryset=Car.objects.select_related("manufacturer"))
    )
