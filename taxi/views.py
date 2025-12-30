from django.shortcuts import render
from django.views import generic

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer").order_by("model")
    context_object_name = "car_list"
    paginate_by = 5
    template_name = "taxi/car_list.html"


class CarDetailView(generic.DetailView):
    model = Car
    context_object_name = "car_detail"
    template_name = "taxi/car_detail.html"


class DriverListView(generic.ListView):
    model = Driver
    queryset = Driver.objects.order_by("username")
    context_object_name = "driver_list"
    paginate_by = 5
    template_name = "taxi/driver_list.html"


class DriverDetailView(generic.DetailView):
    model = Driver
    context_object_name = "driver_detail"
    queryset = Driver.objects.prefetch_related(
        "cars__manufacturer"
    ).order_by("username")
    template_name = "taxi/driver_detail.html"
