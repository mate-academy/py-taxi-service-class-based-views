from django.urls import path

from .views import (
    index,
    ManufacturerListView,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturer-list/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),
    path(
        "car-list/",
        CarListView.as_view(),
        name="car-list"
    ),
    path(
        "car-list/<int:pk>",
        CarDetailView.as_view(),
        name="car-detail"
    ),
    path(
        "driver-list/",
        DriverListView.as_view(),
        name="driver-list"
    ),
    path(
        "driver-list/<int:pk>",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
]

app_name = "taxi"
