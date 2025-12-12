from django.shortcuts import render
from django.views.generic import ListView, DetailView

from taxi.models import Driver, Car, Manufacturer


def index(request):
    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"


class CarListView(ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer").all().order_by("id")
    template_name = "taxi/car_list.html"


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"

    def get_queryset(self):
        return Car.objects.select_related(
            "manufacturer"
        ).prefetch_related("drivers")


class DriverListView(ListView):
    model = Driver
    paginate_by = 5
    queryset = Driver.objects.all().order_by("username")
    template_name = "taxi/driver_list.html"


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"

    def get_queryset(self):
        return Driver.objects.prefetch_related("cars__manufacturer")
