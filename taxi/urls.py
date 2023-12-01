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
    path("manufacturers/",
         ManufacturerListView.as_view(),
         name="manufacturers"),
    path("cars/",
         CarListView.as_view(),
         name="cars"),
    path("cars/<int:pk>/"
         , CarDetailView.as_view(),
         name="car_detail"),
    path("drivers/",
         DriverListView.as_view(),
         name="drivers"),
    path("drivers/<int:pk>/",
         DriverDetailView.as_view(),
         name="driver_detail"),
]

app_name = "taxi"
