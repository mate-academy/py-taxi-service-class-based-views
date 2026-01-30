from django.db.models import Prefetch
from django.views.generic import DetailView, ListView

from taxi.models import Car, Driver, Manufacturer


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer").all()


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related(
        Prefetch(
            "cars",
            queryset=Car.objects.select_related("manufacturer"),
        )
    )
