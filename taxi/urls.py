from django.urls import path

from . import views
from .views import (
    index, CarListView, DriverListView, ManufacturerListView,
    CarDetailView, DriverDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("taxi/cars/", CarListView.as_view(), name="car-list"),
    path("taxi/cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("taxi/drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "taxi/drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
    path(
        "taxi/manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),
]

app_name = "taxi"
