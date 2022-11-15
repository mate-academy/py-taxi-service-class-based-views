from django.urls import path

from .views import (
    index,
    CarListView,
    DriverListView,
    ManufacturerListView,
    CarDetailedView,
    DriverDetailedView,
)

urlpatterns = [
    path("", index, name="index"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path("cars/<int:pk>/", CarDetailedView.as_view(), name="car-detail"),
    path(
        "drivers/<int:pk>/", DriverDetailedView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
