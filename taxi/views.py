from django.shortcuts import render
from django.views import generic

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
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car
    temlate_name = "taxi/manufacturer_detail.html"

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        manufacturer = car.manufacturer
        context["manufacturer"] = manufacturer
        return context


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver_instance"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars_of_driver"] = self.object.cars.all()
        return context
