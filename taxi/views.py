from django.shortcuts import render

from taxi.models import Driver, Car, Manufacturer
from django.views import generic


def index(request):

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
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    context_object_name = "car_list"
    paginate_by = 5
    template_name = "taxi/car_list.html"
    queryset = Car.objects.select_related("manufacturer").order_by("id")


class CarDetailView(generic.DetailView):
    model = Car
    queryset = (Car.objects.select_related("manufacturer")
                .order_by("manufacturer__name")
                .prefetch_related("drivers"))


class DriverListView(generic.ListView):
    model = Driver
    context_object_name = "driver_list"
    template_name = "taxi/driver_list.html"
    queryset = Driver.objects.all().order_by("id")
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
