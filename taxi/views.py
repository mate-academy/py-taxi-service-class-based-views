from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Prefetch
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
    ordering = ["name"]
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer").order_by("id")
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    queryset = Driver.objects.order_by("username")
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related(
        Prefetch(
            "cars",
            queryset=Car.objects.select_related("manufacturer")
        )
    )
