from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Driver, Car, Manufacturer


def index(request):
    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }
    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    paginate_by = 5
    queryset = Manufacturer.objects.all().order_by("name")
    context_object_name = "manufacturer_list"


class CarListView(ListView):
    model = Car
    paginate_by = 5
    context_object_name = "car_list"

    def get_queryset(self):
        return Car.objects.select_related("manufacturer").all().order_by(
            "manufacturer__name", "model"
        )


class CarDetailView(DetailView):
    model = Car
    context_object_name = "car"


class DriverListView(ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"
    paginate_by = 5
    queryset = Driver.objects.all().order_by("username")


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver"
    queryset = Driver.objects.prefetch_related(
        "cars__manufacturer"
    )
