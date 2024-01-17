from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView

from taxi.models import Driver, Car, Manufacturer


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
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("cars__manufacturer")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = self.object.cars.all()
        return context
