from django.views.generic import ListView, DetailView, TemplateView
from .models import Manufacturer, Car, Driver


class IndexView(TemplateView):
    template_name = "taxi/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_drivers"] = Driver.objects.count()
        context["num_cars"] = Car.objects.count()
        context["num_manufacturers"] = Manufacturer.objects.count()
        return context


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer").all()
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car
    queryset = Car.objects.select_related("manufacturer").all()


class DriverListView(ListView):
    model = Driver
    queryset = Driver.objects.order_by("username")
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
