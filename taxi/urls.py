from django.urls import path

from .views import index
from . import views

urlpatterns = [
    path("", index, name="index"),

    path(
        "manufacturers/",
        views.ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),

    path("cars/", views.CarListView.as_view(), name="car-list"),
    path(
        "car/<int:pk>/",
        views.CarDetailView.as_view(),
        name="car-detail"
    ),

    path("drivers/", views.DriverListView.as_view(), name="driver-list"),
    path(
        "driver/<int:pk>/",
        views.DriverDetailView.as_view(),
        name="driver-detail"
    ),
]

app_name = "taxi"
