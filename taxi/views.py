from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Prefetch

from taxi.models import Driver, Car, Manufacturer


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
    queryset = Manufacturer.objects.order_by('name')
    paginate_by = 5
    template_name = 'taxi/manufacturer_list.html'


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related('manufacturer').order_by('model')
    paginate_by = 5
    template_name = 'taxi/car_list.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'taxi/car_detail.html'


class DriverListView(ListView):
    model = Driver
    queryset = Driver.objects.order_by('username')
    paginate_by = 5
    template_name = 'taxi/driver_list.html'


class DriverDetailView(DetailView):
    model = Driver
    template_name = 'taxi/driver_detail.html'

    def get_queryset(self):
        return Driver.objects.prefetch_related(
            Prefetch('cars', queryset=Car.objects.select_related('manufacturer'))
        )
