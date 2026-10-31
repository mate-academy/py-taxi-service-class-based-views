from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Manufacturer, Car, Driver


class ManufacturerListView(LoginRequiredMixin, ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by('name')
    paginate_by = 5


class CarListView(LoginRequiredMixin, ListView):
    model = Car
    queryset = Car.objects.select_related('manufacturer')
    paginate_by = 5


class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car


class DriverListView(LoginRequiredMixin, ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(LoginRequiredMixin, DetailView):
    model = Driver

    def get_queryset(self):
        return Driver.objects.prefetch_related('cars__manufacturer')
