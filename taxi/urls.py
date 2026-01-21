from django.urls import path

from .views import (
    index, manufacturer_list_view,
    CarListView, DriverListView,
    car_detail_view, DriverDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        manufacturer_list_view,
        name="manufacturer-list"
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", car_detail_view, name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
]

app_name = "taxi"
