from django.urls import path

from taxi.views import (
    index,
    CarDetailView,
    ManufacturerListView,
    CarListView,
    DriverListView,
    DriverDetailView,
)


urlpatterns = [
    path(
        "",
        index,
        name="index"
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
    ),
    path(
        "cars/",
        CarListView.as_view(),
        name="car-list"
    ),
    path(
        "drivers/",
        DriverListView.as_view(),
        name="driver-list"
    ),
]
app_name = "taxi"
