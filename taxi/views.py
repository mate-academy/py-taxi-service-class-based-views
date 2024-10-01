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
    model = Manufacturer  # Set the model
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5  # Set pagination to 5 items per page
    template_name = "taxi/manufacturer_list.html"


class CarListView(ListView):
    model = Car
    paginate_by = 5
    template_name = "taxi/car_list.html"

    def get_queryset(self):
        return Car.objects.all().select_related("manufacturer").all()


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(ListView):
    model = Driver
    paginate_by = 5
    template_name = "taxi/driver_list.html"


class DriverDetailView(CarDetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
