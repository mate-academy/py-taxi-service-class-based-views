from django.shortcuts import render

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
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"
    context_object_name = "car_detail"


class DriverListView(ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    context_object_name = "driver_detail"
    queryset = Driver.objects.prefetch_related("cars__manufacturer")

    def get_context_data(self, **kwargs):
        contexts = super().get_context_data(**kwargs)
        contexts["cars"] = self.object.cars.select_related("manufacturer")
        return contexts
