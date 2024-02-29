from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": get_user_model().objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    paginate_by = 5


class CarDetailView(generic.DetailView):
    queryset = Car.objects.prefetch_related("drivers")


class DriverListView(generic.ListView):
    model = get_user_model()
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    queryset = get_user_model().objects.prefetch_related("cars")
