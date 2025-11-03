from django.shortcuts import render
from django.views import generic
from taxi.models import Driver, Car, Manufacturer


def index(request):
    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class DriverListView(generic.ListView):
    model = Driver
    template_name = "taxi/drivers_list.html"
    queryset = Driver.objects.all()
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars")


class CarListView(generic.ListView):
    model = Car
    template_name = "taxi/cars_list.html"
    queryset = Car.objects.all()
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car
    queryset = Car.objects.select_related(
        "manufacturer"
        ).prefetch_related("drivers")


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    template_name = "taxi/manufacturers_list.html"
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5
