from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from taxi.models import Driver, Car, Manufacturer


def index(request):
    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"


class CarListView(ListView):
    model = Car
    paginate_by = 5
    template_name = "taxi/car_list.html"


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["manufacturer"] = self.object.manufacturer
        context["drivers"] = self.object.drivers.all()
        return context


class DriverListView(ListView):
    model = Driver
    paginate_by = 5
    template_name = "taxi/driver_list.html"


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"

    def get_queryset(self):
        return Driver.objects.prefetch_related("cars").all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = self.object.cars.all()
        return context
