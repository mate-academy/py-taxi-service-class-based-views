from django.urls import path

from .views import index

from taxi.views import (
    ManufacturerListView,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),  # имя совпадает с тестами
    path(
        "cars/",
        CarListView.as_view(),
        name="car-list"),                             # имя совпадает с тестами
    path(
        "cars/<int:pk>/",
        CarDetailView.as_view(),
        name="car-detail"
    ),
    path(
        "drivers/",
        DriverListView.as_view(),
        name="driver-list"),                    # имя совпадает с тестами
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
]

app_name = "taxi"
