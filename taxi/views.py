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
    paginate_by = 5
    queryset = Manufacturer.objects.all().order_by("name")
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"


class CarListView(generic.ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer")
    context_object_name = "car_list"
    template_name = "taxi/car_list.html"


class CarDetailView(generic.DetailView):
    model = Car
    context_object_name = "car_info"
    template_name = "taxi/car_detail.html"


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    context_object_name = "driver_list"
    template_name = "taxi/driver_list.html"


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.all()
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver_info"
    slug_field = "username"
    slug_url_kwarg = "username"
