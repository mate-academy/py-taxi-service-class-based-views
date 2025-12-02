from django.http import HttpRequest, Http404
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


class CarsListView(generic.ListView):
    model = Car
    context_object_name = "car_list"
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer")


class CarDetailView(generic.DetailView):
    model = Car


class DriversListView(generic.ListView):
    model = Driver
    context_object_name = "driver_list"
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")


class ManufacturersListView(generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    queryset = Manufacturer.objects.all()
    paginate_by = 5


# Function based view:
# def car_list_view(request: HttpRequest):
#     context = {
#         "car_list": Car.objects.all(),
#     }
#
#     return render(request, "taxi_service/car_list.html", context=context)


# def car_detail_view(request, pk: int):
#     try:
#         car = Car.objects.get(id=pk)
#     except Car.DoesNotExist:
#         raise Http404("Car does not exist")
#     context = {
#         "car": car,
#     }
#
#     return render(request, "taxi_service/car_detail.html", context=context)
