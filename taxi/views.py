from __future__ import annotations

from django.db.models import Prefetch
from django.views.generic import TemplateView, ListView, DetailView

from .models import Manufacturer, Car, Driver

# Configuração compartilhada para melhorar manutenção
DEFAULT_PAGINATE_BY = 5


class IndexView(TemplateView):
    template_name = "taxi/index.html"


class ManufacturerListView(ListView):
    model = Manufacturer
    paginate_by = DEFAULT_PAGINATE_BY
    # Queryset explícito para clareza e testabilidade
    queryset = Manufacturer.objects.order_by("name")


class CarListView(ListView):
    model = Car
    paginate_by = DEFAULT_PAGINATE_BY
    # Evita N+1 carregando o fabricante
    queryset = Car.objects.select_related("manufacturer").order_by("id")


class CarDetailView(DetailView):
    model = Car
    # Otimiza relacionamentos no detalhe do carro
    queryset = (
        Car.objects.select_related("manufacturer")
        .prefetch_related("drivers")
    )


class DriverListView(ListView):
    model = Driver
    paginate_by = DEFAULT_PAGINATE_BY
    queryset = Driver.objects.order_by("id")


class DriverDetailView(DetailView):
    model = Driver
    # Evita N+1 ao carregar fabricantes dos carros do motorista
    queryset = Driver.objects.prefetch_related(
        Prefetch(
            "cars",
            queryset=Car.objects.select_related("manufacturer").order_by("id"),
        )
    )
