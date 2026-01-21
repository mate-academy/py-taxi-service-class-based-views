from django.views.generic import TemplateView, ListView, DetailView
from .models import Manufacturer, Car, Driver
from django.db.models import Prefetch


class HomeView(TemplateView):
    template_name = "home.html"


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer").all()


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"

    def get_queryset(self):

        return super().get_queryset().prefetch_related("cars")
