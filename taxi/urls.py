from django.urls import path

from .views import index, ManufacturerListView, CarListView,\
    DriverListView, DriverDetailView, CarDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufactures/",
         ManufacturerListView.as_view(),
         name="manufacturer_list"),
    path("cars/",
         CarListView.as_view(),
         name="car_list"),
    path("drivers/",
         DriverListView.as_view(),
         name="driver_list"),
    path("drivers/<int:pk>/",
         DriverDetailView.as_view(),
         name="driver-detail"),
    path("cars/<int:pk>/",
         CarDetailView.as_view(),
         name="cars-detail")
]

app_name = "taxi"
