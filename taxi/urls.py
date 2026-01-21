from django.urls import path

from taxi.views import (
    ManufacturerListView,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    HomePageView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"
    ),
]

app_name = "taxi"
