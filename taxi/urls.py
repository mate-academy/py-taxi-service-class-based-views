from django.urls import path

from .views import (
    index,
    ManufacturerListView,
    CarListView,
    DriverListView,
    CarDetailView,
    DriverDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("manufactures/",
         ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("cars/",
         CarListView.as_view(),
         name="car-list"),
    path("drivers/",
         DriverListView.as_view(),
         name="driver-list"),
    path("car/<int:pk>/",
         CarDetailView.as_view(),
         name="car-detail"),
    path("driver/<int:pk>/",
         DriverDetailView.as_view(),
         name="driver-detail"),
]

app_name = "taxi"
