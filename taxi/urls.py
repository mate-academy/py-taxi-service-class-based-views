from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "Manufacturer-list/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),
    path(
        "Car-list/",
        CarListView.as_view(),
        name="car-list"
    ),
    path(
        "Car-detail/<int:pk>",
        CarDetailView.as_view(),
        name="car-detail"
    ),
    path(
        "Driver-list/",
        DriverListView.as_view(),
        name="driver-list"
    ),
    path(
        "Driver-detail/<int:pk>",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
]

app_name = "taxi"
