from django.shortcuts import render
from django.views import generic

from taxi.models import Driver, Car, Manufacturer


class IndexView(generic.TemplateView):
    template_name = "taxi/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_drivers"] = Driver.objects.count()
        context["num_cars"] = Car.objects.count()
        context["num_manufacturers"] = Manufacturer.objects.count()
        return context


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    queryset = (
        Car.objects.all().
        order_by("model").
        select_related("manufacturer").
        prefetch_related("drivers")
    )
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car
    queryset = Car.objects.all().select_related("manufacturer")


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars")
