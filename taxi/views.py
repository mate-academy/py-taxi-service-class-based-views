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
    context_object_name = "manufacturer_list"


class CarListView(ListView):
    queryset = Car.objects.select_related("manufacturer").order_by("model")
    paginate_by = 5
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(ListView):
    model = Driver
    queryset = Driver.objects.all().order_by("username")
    paginate_by = 5
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"


class DriverDetailView(DetailView):
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
    template_name = "taxi/driver_detail.html"
