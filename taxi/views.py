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
    context_object_name = "manufacturer_list"  # Updated
    paginate_by = 5
    queryset = Manufacturer.objects.order_by("name")
    template_name = "taxi/manufacturer_list.html"


class DriverListView(generic.ListView):
    model = Driver
    context_object_name = "driver_list"  # Updated
    paginate_by = 5
    queryset = Driver.objects.order_by("is_active")
    template_name = "taxi/driver_list.html"


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"

    def get_queryset(self):
        return Driver.objects.prefetch_related("cars__manufacturer")


class CarListView(generic.ListView):
    model = Car
    context_object_name = "car_list"  # Updated
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer")
    template_name = "taxi/car_list.html"


class CarDetailView(generic.DetailView):
    model = Car
    context_object_name = "car"
    template_name = "taxi/car_detail.html"
