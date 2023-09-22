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
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = (
        Car.objects.select_related("manufacturer").all().order_by("model")
    )
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car

    def get_object(self, queryset=None):
        return (
            Car.objects.select_related("manufacturer")
            .prefetch_related("drivers")
            .get(id=self.kwargs["pk"])
        )

    def get_context_data(self, **kwargs):
        car = self.object
        context = super().get_context_data(
            object_list=car.drivers.all(),
            **kwargs  # to use in car-detail.html
        )
        return context


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView, MultipleObjectMixin):
    model = Driver
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
