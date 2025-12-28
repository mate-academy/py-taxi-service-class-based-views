from django.urls import path

from .views import (index,
                    ManufacturerListView,
                    CarListView,
                    DriverListView,
                    CarDetailView,
                    DriverDetailView)

urlpatterns = [
    path("", index, name="index"),
    path("Manufacturer", ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("Car", CarListView.as_view(), name="car-list"),
    path("Driver", DriverListView.as_view(), name="driver-list"),
    path("Car/<int:pk>", CarDetailView.as_view(), name="car-detail"),
    path("Driver/<int:pk>", DriverDetailView.as_view(), name="driver-detail"),
]

app_name = "taxi"
