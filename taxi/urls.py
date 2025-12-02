from __future__ import annotations

from django.urls import path

from .views import (
    CarDetailView,
    CarListView,
    DriverDetailView,
    DriverListView,
    ManufacturerListView,
    IndexView,
)

app_name = "taxi"

urlpatterns = [
    path(
        "",
        IndexView.as_view(),
        name="index",
    ),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "cars/",
        CarListView.as_view(),
        name="car-list",
    ),
    path(
        "cars/<int:pk>/",
        CarDetailView.as_view(),
        name="car-detail",
    ),
    path(
        "drivers/",
        DriverListView.as_view(),
        name="driver-list",
    ),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail",
    ),
]
