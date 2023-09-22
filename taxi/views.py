from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from .models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    queryset = Manufacturer.objects.all().order_by("name")
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = (
        Car.objects.select_related("manufacturer").all().order_by("model")
    )
    template_name = "taxi/car_list.html"
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car
    context_object_name = "car"

    def get_object(self, queryset=None):
        return (
            Car.objects.select_related("manufacturer")
            .prefetch_related("drivers")
            .get(id=self.kwargs["pk"])
        )

    def get_context_data(self, **kwargs):
        car = self.object
        context = super().get_context_data(
            object_list=car.drivers.all(), **kwargs
        )
        return context


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView, MultipleObjectMixin):
    model = Driver
    context_object_name = "driver"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        driver = self.get_object()
        object_list = (
            Driver.objects.prefetch_related("cars", "cars__manufacturer")
            .get(id=driver.id)
            .cars.all()
        )
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context
