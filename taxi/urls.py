from django.urls import path

from taxi.views import (
    index,
    ManufacturerListView,
    CarDetailView,
    CarListView,
    DriverListView,
    DriverDetailView
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
        name="manufacturer_list_view"
    ),
    path(
        "cars/",
        CarListView.as_view(),
        name="car_list_view"
    ),
    path(
        "cars/<int:pk>/",
        CarDetailView.as_view(),
        name="car_detail_view"
    ),
    path(
        "drivers/",
        DriverListView.as_view(),
        name="driver_list_view"
    ),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver_detail_view"
    )
]

app_name = "taxi"
