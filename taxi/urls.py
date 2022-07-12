from django.urls import path

from .views import index, ManufacturerListView, CarListView, CarDetailView, DriverListView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path(
        "Manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturers-list"
    ),
    path(
        "Cars/",
        CarListView.as_view(),
        name="cars-list"
    ),
    path(
        "Cars/<int:pk>/",
        CarDetailView.as_view(),
        name="cars-detail"
    ),
    path(
        "Drivers/",
        DriverListView.as_view(),
        name="drivers-list"
    ),
    path(
        "Drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="drivers-detail"
    ),
]


app_name = "taxi"
