from django.views.generic import ListView, DetailView
from .models import Car, Driver, Manufacturer
from django.shortcuts import render


def index(request):
    num_cars = Car.objects.count()
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_cars": num_cars,
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
    }
    return render(request, "taxi/index.html", context)


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Manufacturer.objects.all().order_by("name")


class CarListView(ListView):
    model = Car
    template_name = "taxi/car_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Car.objects.select_related("manufacturer").order_by("id")


class CarDetailView(DetailView):
    model = Car
    template_name = "taxi/car_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["drivers"] = self.object.drivers.all()
        return context


class DriverListView(ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Driver.objects.all().order_by("id")  # Order by driver ID


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"

    def get_queryset(self):
        return Driver.objects.prefetch_related("cars__manufacturer").all()
