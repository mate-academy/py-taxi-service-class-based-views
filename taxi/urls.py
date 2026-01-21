from django.urls import path

from taxi.views import (
    ManufacturerListView,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
)
from . import views
from .views import index


app_name = "taxi"


urlpatterns = [
    path(
        "",
        index,
        name="index",
    ),
    path(
        "cars/",
        views.CarListView.as_view(),
        name="car-list",
    ),
    path(
        "cars/<int:pk>/",
        views.CarDetailView.as_view(),
        name="car-detail",
    ),
    path(
        "drivers/",
        views.DriverListView.as_view(),
        name="driver-list",
    ),
    path(
        "drivers/<int:pk>/",
        views.DriverDetailView.as_view(),
        name="driver-detail",
    ),
    path(
        "manufacturers/",
        views.ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
]
