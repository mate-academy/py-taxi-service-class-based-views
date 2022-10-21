from django.urls import path

from .views import index, ManufacturerListViews, CarListViews, DriverListViews, car_detail_view, driver_detail_view

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListViews.as_view(),
         name="manufacturer-list"),
    path("cars/", CarListViews.as_view(), name="car-list"),
    path("drivers/", DriverListViews.as_view(), name="driver-list"),
    path("cars/<int:pk>", car_detail_view, name="car-detail"),
    path("drivers/<int:pk>", driver_detail_view, name="driver-detail"),
]

app_name = "taxi"
