from django.urls import path

from taxi.views import (index,
                        ManufacturerListView,
                        DriverListView,
                        CarListView,
                        CarDetailView,
                        DriverDetailView)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturer/",
         ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("driver/", DriverListView.as_view(), name="driver-list"),
    path("car/", CarListView.as_view(), name="car-list"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/<int:pk>/",
         DriverDetailView.as_view(),
         name="driver-detail"),
]

app_name = "taxi"

