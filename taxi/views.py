from django.views import generic
from django.contrib.auth import get_user_model

from .models import Manufacturer, Car


Driver = get_user_model()


class HomeView(generic.TemplateView):
    template_name = "taxi/home.html"


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer").order_by("id")
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = (
        Driver.objects.prefetch_related("cars__manufacturer").order_by("id")
    )
