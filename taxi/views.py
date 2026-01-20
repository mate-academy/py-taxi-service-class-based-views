from django.http import HttpRequest, HttpResponse
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

    def get_queryset(self):
        return Manufacturer.objects.all().order_by("name")


class CarListView(generic.ListView):
    model = Car
    context_object_name = "car_list"
    paginate_by = 5

    def get_queryset(self):
        return Car.objects.select_related("manufacturer")


def car_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    car = Car.objects.get(pk=pk)
    context = {
        "car": car,
    }
    return render(request, "taxi/car_detail.html", context=context)


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver"

    def get_queryset(self):
        return Driver.objects.prefetch_related("cars__manufacturer").all()
