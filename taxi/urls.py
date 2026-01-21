from django.urls import path

from .views import (
    index,
    ManufacturerListView,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/",
         ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>", DriverDetailView.as_view(), name="driver-detail")
]

app_name = "taxi"
