from django.urls import path

from .views import (
    index, ManufacturerListView, CarListView,
    DriverListView, CarDetailView, DriverDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufactures/", ManufacturerListView.as_view(),
        name="manufactures_list"
    ),
    path("cars/", CarListView.as_view(), name="cars_list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
    path("drivers/", DriverListView.as_view(), name="drivers_list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(),
        name="driver_detail"
    ),
]

app_name = "taxi"
