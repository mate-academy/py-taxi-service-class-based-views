from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic

from taxi.models import Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": get_user_model().objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ListViewWithPagination(generic.ListView):
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        if context.get("is_paginated"):
            paginator = context.get("paginator")
            page_obj = context.get("page_obj")
            context["page_range"] = paginator.get_elided_page_range(
                number=page_obj.number, on_each_side=2, on_ends=2
            )
        return context


class ManufacturerListView(ListViewWithPagination):
    model = Manufacturer
    queryset = Manufacturer.objects.all()
    paginate_by = 5


class CarListView(ListViewWithPagination):
    model = Car
    queryset = (
        Car.objects.all().select_related("manufacturer").order_by("model")
    )
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(ListViewWithPagination):
    model = get_user_model()
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = get_user_model()
    queryset = get_user_model().objects.prefetch_related(
        "cars", "cars__manufacturer"
    )
