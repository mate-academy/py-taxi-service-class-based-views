from django.urls import path

from .views import (ManufacturerListView,
                    DriverListView,
                    DriverDetailView,
                    CarDetailView,
                    CarListView)

app_name = "taxi"

urlpatterns = [
    path("manufacturers/", ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("drivers/", DriverListView.as_view(),
         name="driver-list"),
    path("cars/", CarListView.as_view(),
         name="car-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(),
         name="driver-detail"),
    path("cars/<int:pk>/", CarDetailView.as_view(),
         name="car-detail"),
]
