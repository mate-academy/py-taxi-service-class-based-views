from django.urls import path

from .views import (index, CarListView, CarDetailView,
                    DriverListView, DriverDetailView, ManufacturerListView)


urlpatterns = [
    path("", index, name="index"),
    path("manufacturer/", ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("driver/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car-detail")
]

app_name = "taxi"
