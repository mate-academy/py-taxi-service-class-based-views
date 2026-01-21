from django.urls import path

from .views import (
    index,
    ManufacturerListView,
    DriverDetailView,
    DriverListView,
    CarListView,
    CarDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/",
         ManufacturerListView.as_view(),
         name="manufacturer_list"),
    path("drivers/", DriverListView.as_view(),
         name="driver_list"),
    path("drivers/<int:pk>/",
         DriverDetailView.as_view(),
         name="driver_detail"),
    path("cars/", CarListView.as_view(), name="car_list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
]

app_name = "taxi"
