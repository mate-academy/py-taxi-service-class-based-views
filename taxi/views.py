from django.shortcuts import render
from taxi.models import Driver, Car, Manufacturer
from django.views.generic import ListView, DetailView
from django.db.models import Prefetch


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
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5
    template_name = "taxi/car_list.html"


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(ListView):
    model = Driver
    paginate_by = 5
    template_name = "taxi/driver_list.html"


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related(
        Prefetch("cars",
                 queryset=Car.objects.select_related("manufacturer"))
    )
    template_name = "taxi/driver_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = self.object.cars.all()
        return context
