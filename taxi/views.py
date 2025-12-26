from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from taxi.models import Driver, Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all()
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"


class CarListView(generic.ListView):
    model = Car
    queryset = (
        Car.objects.select_related("manufacturer").
        prefetch_related("drivers").all()
    )
    paginate_by = 5
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"


class CarDetailView(generic.DetailView):
    model = Car
    template_name = "taxi/car_detail.html"
    context_object_name = "car_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        drivers = car.drivers.all()
        manufacturer = car.manufacturer
        context["manufacturer"] = manufacturer
        context["drivers"] = drivers
        return context


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        driver = self.get_object()
        cars = Car.objects.filter(drivers=driver)
        context["cars"] = cars
        return context
