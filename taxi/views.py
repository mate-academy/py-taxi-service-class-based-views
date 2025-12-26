from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views import generic

from taxi.models import Driver, Car, Manufacturer


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    queryset = Car.objects.prefetch_related("manufacturer", "drivers")
    paginate_by = 5


class DriverListView(generic.ListView):
    model = Driver
    queryset = Driver.objects.prefetch_related(
        "cars__manufacturer",
        "cars__drivers"
    )
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver


class CarDetailView(generic.DetailView):
    model = Car


class ManufacturerCreateView(generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "taxi/manufacturer_create_form.html"


class ManufacturerUpdateView(generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "taxi/manufacturer_create_form.html"


class ManufacturerDeleteView(generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("taxi:manufacturer-list")
    template_name = "taxi/manufacturer_delete_confirm.html"


class CarCreateView(generic.CreateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")
    template_name = "taxi/car_create_form.html"


class CarUpdateView(generic.UpdateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("taxi:car-list")
    template_name = "taxi/car_create_form.html"


class CarDeleteView(generic.DeleteView):
    model = Car
    success_url = reverse_lazy("taxi:car-list")
    template_name = "taxi/car_delete_confirm.html"
