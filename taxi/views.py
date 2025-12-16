from django.views.generic import ListView, DetailView
from django.db.models import Prefetch
from .models import Manufacturer, Car, Driver
from django.views.generic import TemplateView


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer").all().order_by("id")
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related(
        Prefetch("cars", queryset=Car.objects.select_related("manufacturer"))
    )


class HomePageView(TemplateView):
    template_name = "taxi/home.html"
