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
    paginate_by = 5
    queryset = Manufacturer.objects.order_by(
        "name")


class CarListView(generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    queryset = Car.objects.select_related("manufacturer").order_by("model")
    context_object_name = "car_list"
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(generic.ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"
    queryset = Driver.objects.order_by("username")
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    queryset = Driver.objects.all().prefetch_related("cars__manufacturer")
