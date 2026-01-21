from typing import ClassVar

from django.db.models import Prefetch
from django.shortcuts import render
from django.views import generic

from taxi.mixins import BaseTableMixin
from taxi.models import Car, Driver, Manufacturer
from taxi.table_spec import TableKey


def index(request):
    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }
    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(BaseTableMixin, generic.ListView):
    model = Manufacturer
    paginate_by = 5
    table_spec_key: ClassVar[TableKey] = "manufacturers"


class CarListView(BaseTableMixin, generic.ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer")
    table_spec_key: ClassVar[TableKey] = "cars"


class DriverListView(BaseTableMixin, generic.ListView):
    model = Driver
    paginate_by = 5
    table_spec_key: ClassVar[TableKey] = "drivers"


class CarDetailView(generic.DetailView):
    model = Car
    queryset = (
        Car.objects
        .select_related("manufacturer")
        .prefetch_related("drivers")
    )


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related(
        Prefetch(
            "cars",
            queryset=Car.objects.select_related("manufacturer"),
        )
    )
