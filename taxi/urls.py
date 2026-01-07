from django.urls import path

from .views import (
    index,
    DriversView,
    DriversDetailView,
    CarsView,
    CarsDetailView,
    ManufacturersView
)

urlpatterns = [
    path("", index, name="index"),
    path("drivers/", DriversView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>",
        DriversDetailView.as_view(),
        name="driver-detail"
    ),
    path("cars/", CarsView.as_view(), name="car-list"),
    path("cars/<int:pk>", CarsDetailView.as_view(), name="car-detail"),
    path(
        "manufacturers/",
        ManufacturersView.as_view(),
        name="manufacturer-list"
    ),
]

app_name = "taxi"
