from django.shortcuts import render
from taxi.models import Driver, Car, Manufacturer
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = (Car.objects.select_related("manufacturer").all()
                .order_by("model"))
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car

    def get_queryset(self):
        return (Car.objects.select_related("manufacturer")
                .prefetch_related("drivers"))


class DriverListView(ListView):
    model = Driver
    queryset = (Driver.objects.prefetch_related("cars__manufacturer").all()
                .order_by("username"))
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)
