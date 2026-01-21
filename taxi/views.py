from django.db.models import QuerySet
from django.shortcuts import render
from django.views import generic

from taxi.models import Driver, Car, Manufacturer


def index(request):
    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(
        request,
        "taxi/index.html",
        context=context
    )


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all()
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver

    context_object_name = "driver_detail"

    def get_queryset(self) -> QuerySet:
        pk = self.kwargs["pk"]
        return (
            Driver.objects.filter(pk=pk)
            .prefetch_related("cars__manufacturer")
        )


class CarDetailView(generic.DetailView):
    model = Car

    context_object_name = "car_detail"
