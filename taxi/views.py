from django.shortcuts import render

from taxi.models import Driver, Car, Manufacturer
from django.views.generic import ListView, DetailView

def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(
        request,
        "taxi/index.html",
        context=context)

class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    queryset = Manufacturer.objects.all()
    paginate_by = 5

class CarListView(ListView):
    model = Car
    template_name = "taxi/car_list.html"
    queryset = (
        Car.objects.all()
        .select_related("manufacturer")
        .prefetch_related("drivers"))
    paginate_by = 5

class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"

class DriverListView(ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    paginate_by = 5

class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
