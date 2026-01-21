from django.views.generic import ListView, DetailView

from django.shortcuts import render

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
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer").order_by("model")
    context_object_name = "car_list"


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    paginate_by = 5
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
    context_object_name = "driver_list"


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars").order_by("username")
