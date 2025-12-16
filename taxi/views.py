from django.shortcuts import render
from django.views import generic
from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    paginate_by = 5
    template_name = "taxi/car_list.html"
    queryset = Car.objects.select_related("manufacturer")


class CarDetailView(generic.DetailView):
    model = Car
    template_name = "taxi/car_detail.html"
    context_object_name = "car"
    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #     return Car.objects.get(id = pk)


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    template_name = "taxi/driver_list.html"
    # queryset = Driver.objects.select_related("cars")


class DriverDetailView(generic.DetailView):
    model = Driver
    # context_object_name = "cars"
    template_name = "taxi/driver_detail.html"
    slug_field = "username"
    slug_url_kwarg = "slug"
