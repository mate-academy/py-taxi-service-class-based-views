from django.urls import path

from .views import index, ManufacturerListView, CarListView, DriverListView, DriverDetailView, CarDetailView, ManufacturerDetailView



urlpatterns = [
    path("", index, name="index"),
    path(
        "manufactures/", ManufacturerListView.as_view(), name="manufactures-list"
    ),
    path(
        "manufactures/<int:pk>/",
         ManufacturerDetailView.as_view(),
         name="manufactures-detail"
    ),
    path(
        "cars/",
        CarListView.as_view(),
        name="cars-list",
    ),
    path(
        "cars/<int:pk>/",
         CarDetailView.as_view(),
         name="car-detail"
    ),
    path(
        "drivers/",
         DriverListView.as_view(),
         name="drivers-list"
    ),
    path(
        "drivers/<int:pk>/",
         DriverDetailView.as_view(),
         name="driver-detail"
    ),
]

app_name = "taxi"
