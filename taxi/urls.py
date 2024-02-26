from django.urls import path

from .views import (index,
                    CarListView,
                    ManufacturerListView,
                    CarDetailView,
                    DriverListView,
                    DriverDetailView)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturer/", ManufacturerListView.as_view(), name="manufacturer_list"),
    path("cars/", CarListView.as_view(), name="car_list"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
    path("drivers/", DriverListView.as_view(), name="driver_list"),
    path("driver/<int:pk>/", DriverDetailView.as_view(), name="driver_detail"),
]

app_name = "taxi"
