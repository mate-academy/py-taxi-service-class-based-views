from django.shortcuts import render

from .models import Driver, Car, Manufacturer

from django.views.generic import DetailView, ListView


def index(request):
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "taxi/manufacturer_list.html"
    queryset = model.objects.all().order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    paginate_by = 5
    queryset = model.objects.select_related("manufacturer")


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = model.objects.prefetch_related("cars__manufacturer")
