from django.urls import path

from .views import (
    index,
    DriverListView,
    CarListView,
    ManufacturerListView,
    DriverDetailView,
    CarDetailView)

urlpatterns = [
    path("", index, name="index"),
    path(
        "drivers/",
        DriverListView.as_view(),
        name="driver-list"
    ),
    path(
        "cars/",
        CarListView.as_view(),
        name="car-list"
    ),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
    path(
        "cars/<int:pk>/",
        CarDetailView.as_view(),
        name="car-detail"
    )
]

app_name = "taxi"
