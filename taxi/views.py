from django.shortcuts import render

from django.views import generic

from .models import Manufacturer, Car, Driver


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
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"


class CarListView(generic.ListView):
    model = Car
    paginate_by = 5
    ordering = ["id"]
    # Оптимізація N+1 для виробника
    queryset = Car.objects.select_related("manufacturer")


class CarDetailView(generic.DetailView):
    model = Car
    paginate_by = 5


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    # Оптимізація N+1: підвантажуємо авто драйвера та виробників цих авто
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
