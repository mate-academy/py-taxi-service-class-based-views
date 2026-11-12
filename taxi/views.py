from django.views import generic

from taxi.models import Car, Driver, Manufacturer
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related(
        "cars__manufacturer"
    )
