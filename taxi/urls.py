from django.urls import path

from .views import (
    index,
    ManufacturerListView,
    CarListView,
    DriverListView,
    CarDetailView,
    DriverDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),
    path("car/", CarListView.as_view(), name="car-list"),
    path("car/<int:pk>", CarDetailView.as_view(), name="car-detail"),
    path("driver/", DriverListView.as_view(), name="driver-list"),
    path(
        "driver/<int:pk>",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
]

app_name = "taxi"
