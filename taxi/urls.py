from django.urls import path

from .views import index, ManufacturerListView, CarListView,\
    DriverListView, DriverDetailView, CarDetailView, ManufacturerDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufactures/",
         ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("cars/",
         CarListView.as_view(),
         name="car-list"),
    path("drivers/",
         DriverListView.as_view(),
         name="driver-list"),
    path("drivers/<int:pk>/",
         DriverDetailView.as_view(),
         name="driver-detail"),
    path("cars/<int:pk>/",
         CarDetailView.as_view(),
         name="cars-detail"),
    path("manufacturer/<int:pk>/",
         ManufacturerDetailView.as_view(),
         name="manufactures-detail")
]

app_name = "taxi"
