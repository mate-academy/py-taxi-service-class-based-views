from django.shortcuts import render
from django.template.backends import django
from django.views.generic import ListView, DetailView

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    paginate_by = 5

    def get_queryset(self):
        return Manufacturer.objects.all().order_by("name")


class CarListView(ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer").all()


class CarDetailView(DetailView):
    model = Car

    def get_queryset(self):
        return (Car.objects.select_related("manufacturer")
                .prefetch_related("drivers"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["drivers"] = self.object.drivers.all()

        return context


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars").all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = context["driver"].cars.all()
        return context
