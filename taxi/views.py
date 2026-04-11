from django.db.models import QuerySet
from django.views import generic

from taxi.models import Car, Driver, Manufacturer


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Car]:
        return Car.objects.select_related("manufacturer").all()


class CarDetailView(generic.DetailView):
    model = Car

    def get_queryset(self) -> QuerySet[Car]:
        return Car.objects.select_related("manufacturer").prefetch_related("drivers")


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver

    def get_queryset(self) -> QuerySet[Driver]:
        return Driver.objects.prefetch_related(
            "cars__manufacturer"
        )
