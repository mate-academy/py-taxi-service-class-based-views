from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator

from .models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    num_drivers = Driver.objects.count()
    num_cars = Car.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
    }

    return render(request, "taxi/index.html", context=context)


def manufacturer_list_view(request):
    manufacturer_list = Manufacturer.objects.all().order_by("name")
    paginator = Paginator(manufacturer_list, 5)
    page = request.GET.get("page")
    manufacturer_list_on_page = paginator.get_page(page)

    context = {
        "manufacturer_list": manufacturer_list_on_page,
        "page": page,
    }
    return render(
        request,
        "taxi/manufacturer_list.html",
        context=context
    )


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.all().select_related("manufacturer")
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars")
    paginate_by = 5
