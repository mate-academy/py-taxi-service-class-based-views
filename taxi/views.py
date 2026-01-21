from django.views import generic
from django.views.generic import TemplateView


from taxi.models import Manufacturer, Car, Driver


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5
    template_name = "taxi/manufacturer_list.html"


class CarListView(generic.ListView):
    model = Car
    paginate_by = 5
    template_name = "taxi/car_list.html"

    def get_queryset(self):
        return Car.objects.select_related(
            "manufacturer"
        ).all().order_by("model")


class CarDetailView(generic.DetailView):
    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    template_name = "taxi/driver_list.html"

    def get_queryset(self):
        return Driver.objects.all().order_by("last_name")


class DriverDetailView(generic.DetailView):
    model = Driver
    template_name = "taxi/driver_detail.html"

    def get_queryset(self):
        return Driver.objects.prefetch_related("cars__manufacturer")


class HomePageView(TemplateView):
    template_name = "taxi/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_drivers"] = Driver.objects.count()
        context["num_cars"] = Car.objects.count()
        context["num_manufacturers"] = Manufacturer.objects.count()
        return context
