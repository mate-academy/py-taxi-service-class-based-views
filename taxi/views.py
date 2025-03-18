from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import TemplateView

from taxi.models import Car, Driver, Manufacturer


class HomePageView(TemplateView):
    template_name = "taxi/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["num_cars"] = Car.objects.count()
        context["num_drivers"] = get_user_model().objects.count()
        context["num_manufacturers"] = Manufacturer.objects.count()

        return context


def manufacturers_list_view(request: HttpRequest) -> render:
    paginator = Paginator(Manufacturer.objects.order_by("name"), 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "manufacturer_list": page_obj,
        "is_paginated": paginator.num_pages > 1,
        "paginator": paginator,
        "page_obj": page_obj,
    }
    return render(request, "taxi/manufacturer_list.html", context=context)


class CarsLlistView(generic.ListView):
    model = Car
    paginate_by = 5

    def get_queryset(self) -> QuerySet:
        return self.model.objects.select_related("manufacturer")


class DriversListView(generic.ListView):
    model = Driver
    paginate_by = 5


def manufacturer_detail_view(request: HttpRequest, pk: int) -> render:
    context = {
        "manufacturer": get_object_or_404(Manufacturer, pk=pk)
    }

    return render(request, "taxi/manufacturer_detail.html", context=context)


class CarDetailView(generic.DetailView):
    model = Car


class DriverDetailView(generic.DetailView):
    model = Driver

    def get_queryset(self) -> QuerySet:
        return self.model.objects.prefetch_related("cars__manufacturer")
