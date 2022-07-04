from django.urls import path

from .views import (
    index,
    ManufacturerListView, CarListView, DriverListView,
    CarDetailView, DriverDetailView
)

urlpatterns = [
    path("",
         index,
         name="index"),
    path("cars/",
         CarListView.as_view(),
         name="car"),
    path("cars/<int:pk>",
         CarDetailView.as_view(),
         name="car-detail"),
    path("drivers/",
         DriverListView.as_view(),
         name="driver"),
    path("drivers/<int:pk>",
         DriverDetailView.as_view(),
         name="driver-detail"),
    path("manufacturers/",
         ManufacturerListView.as_view(),
         name="manufacturer"),
]

app_name = "taxi"
