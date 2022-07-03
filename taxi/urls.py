from django.urls import path

from .views import index, ManufacturerListView, \
    CarListView, CarDetailView, DriverListView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufactures/",
        ManufacturerListView.as_view(),
        name="Manufacturer-List",
    ),
    path(
        "cars/",
        CarListView.as_view(),
        name="Car-List",
    ),
    path(
        "cars/<int:pk>/",
        CarDetailView.as_view(),
        name="Car-Detail",
    ),
    path(
        "drivers/",
        DriverListView.as_view(),
        name="Driver-List",
    ),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="Driver-Detail",
    )
]

app_name = "taxi"
