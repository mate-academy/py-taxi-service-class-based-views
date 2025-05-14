from django.core.paginator import Paginator
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


def manufacturer_list_view(request: HttpRequest):
    manufacturers_list = Manufacturer.objects.all().order_by("name")
    paginator = Paginator(manufacturers_list, 5)

    page_number = request.GET.get("page")
    manufacturers_list = paginator.get_page(page_number)

    context = {
        "manufacturer_list": manufacturers_list,
        "page_obj": manufacturers_list,
        "is_paginated": manufacturers_list.has_other_pages(),
        "paginator": paginator,
    }

    return render(
        request,
        "taxi/manufacturer_list.html",
        context=context
    )


class CarListView(generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"
    queryset = (
        Car.objects.all()
        .select_related("manufacturer")
        .prefetch_related("drivers")
    )
    paginate_by = 5


def car_detail_view(request: HttpRequest, pk: int):
    try:
        car = (
            Car.objects
            .select_related("manufacturer")
            .prefetch_related("drivers")
            .get(id=pk)
        )
    except Car.DoesNotExist:
        raise Http404("Car does not exist")

    context = {
        "car": car,
    }

    return render(request, "taxi/car_detail.html", context=context)


class DriverListView(generic.ListView):
    model = Driver
    queryset = Driver.objects.prefetch_related("cars")
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
    queryset = Driver.objects.all().prefetch_related("cars")
    template_name = "taxi/driver_detail.html"
