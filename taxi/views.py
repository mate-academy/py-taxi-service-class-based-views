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
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"
    paginate_by = 5
    queryset = Manufacturer.objects.all().order_by("name")


class CarListView(generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"
    paginate_by = 5

    def get_queryset(self):
        return Car.objects.select_related("manufacturer").all()


class CarDetailView(generic.DetailView):
    model = Car
    template_name = "taxi/car_detail.html"
    context_object_name = "car_detail"


class DriverListView(generic.ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver_detail"
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().prefetch_related("cars__manufacturer")
