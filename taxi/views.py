from django.db.models import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from taxi.models import Car, Driver, Manufacturer


class ManufacturerListView(ListView):
    """Display a paginated list of all manufacturers ordered by name."""

    model = Manufacturer
    queryset: QuerySet = Manufacturer.objects.order_by("name")
    paginate_by: int = 5
    template_name: str = "taxi/manufacturer_list.html"
    context_object_name: str = "manufacturer_list"


class CarListView(ListView):
    """Display a paginated list of cars with manufacturer preloaded."""

    model = Car
    queryset: QuerySet = Car.objects.select_related("manufacturer")
    paginate_by: int = 5
    template_name: str = "taxi/car_list.html"
    context_object_name: str = "car_list"


class CarDetailView(DetailView):
    """Display detail information for a single car."""

    model = Car
    template_name: str = "taxi/car_detail.html"


class DriverListView(ListView):
    """Display a paginated list of all drivers."""

    model = Driver
    paginate_by: int = 5
    template_name: str = "taxi/driver_list.html"
    context_object_name: str = "driver_list"


class DriverDetailView(DetailView):
    """Display detail information for a single driver with their cars."""

    model = Driver
    queryset: QuerySet = Driver.objects.prefetch_related(
        "cars__manufacturer"
    )
    template_name: str = "taxi/driver_detail.html"


def index(request):
    """Render the home page with summary counts."""
    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }
    return render(request, "taxi/index.html", context)
