from msilib.schema import ListView

from django.shortcuts import render

from taxi.models import Driver, Car, Manufacturer


def index(request):

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):

    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturers"
    paginate_by = 5

    @staticmethod
    def get_queryset():
        return Manufacturer.objects.all().order_by("name")

class CarListView(ListView):

    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "cars"
    paginate_by = 5

    @staticmethod
    def get_queryset():
        return Car.objects.select_related("manufacturer").all()

class CarDetailView(DetailView):

    model = Car
    template_name = "taxi/car_detail.html"


class DriverListView(ListView):

    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "drivers"
    paginate_by = 5


class DriverDetailView(DetailView):

    model = Driver
    template_name = "taxi/driver_detail.html"

    @staticmethod
    def get_queryset():
        return Driver.objects.prefetch_related("cars")
