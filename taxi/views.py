from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from taxi.models import Car, Driver, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }
    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer").order_by("id")


class CarDetailView(DetailView):
    model = Car

    def get_queryset(self):  # type: ignore[override]
        return (
            super()
            .get_queryset()
            .select_related("manufacturer")
            .prefetch_related("drivers")
        )


class DriverListView(ListView):
    model = Driver
    paginate_by = 5
    queryset = Driver.objects.all().order_by("username")


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
