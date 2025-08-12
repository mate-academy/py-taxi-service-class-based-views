from django.urls import path

from .views import (
    index,
    CarsListView,
    CarDetailView,
    DriverDetailView,
    DriversListView,
    ManufacturersListView
)

urlpatterns = [
    path(
        "",
        index,
        name="index"
    ),
    path(
        "manufacturers/",
        ManufacturersListView.as_view(),
        name="manufacturer-list"
    ),
    path(
        "cars/",
        CarsListView.as_view(),
        name="car-list"
    ),
    path(
        "cars/<int:pk>/",
        CarDetailView.as_view(),
        name="car-detail"
    ),
    path(
        "drivers/",
        DriversListView.as_view(),
        name="driver-list"
    ),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
]

app_name = "taxi"
