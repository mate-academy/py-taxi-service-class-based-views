from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from taxi.models import Driver, Car, Manufacturer


@login_required
def index(request):
    """View function for the home page of the site."""
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_visits": num_visits + 1
    }

    return render(request, "taxi/index.html", context=context)


class DriverListView(LoginRequiredMixin, generic.ListView):
    model = Driver
    paginate_by = 5


class CarListView(LoginRequiredMixin, generic.ListView):
    model = Car
    queryset = Car.objects.order_by("model").prefetch_related("drivers")
    paginate_by = 5


class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.order_by("name")
    paginate_by = 5


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars")


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car
    queryset = Car.objects.prefetch_related("drivers")
