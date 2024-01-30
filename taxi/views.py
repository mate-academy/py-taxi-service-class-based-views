from django.shortcuts import render
from django.views.generic import ListView, DetailView
from taxi.models import Driver, Car, Manufacturer


def index(request):
    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "url_home": True,
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    extra_context = {"url_manufacturer": True}
    paginate_by = 5


class CarListView(ListView):
    model = Car
    extra_context = {"url_car": True}
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class DriverListView(ListView):
    model = Driver
    extra_context = {"url_driver": True}
    queryset = Driver.objects.prefetch_related("cars")
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car
    extra_context = {"url_car": True}


class DriverDetailView(DetailView):
    model = Driver
    extra_context = {"url_driver": True}
