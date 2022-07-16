from django.urls import path

from .views import index, ManufacturerListView, CarListView, DriverListView, CarDetailView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturer/", ManufacturerListView.as_view(), name="manufacturer_list_view"),
    path("car/", CarListView.as_view(), name="car_list_view"),
    path("car/<int:pk>", CarDetailView.as_view(), name="car_detail"),
    path("driver/", DriverListView.as_view(), name="driver_list_view"),
    path("driver/<int:pk>", DriverDetailView.as_view(), name="driver_detail")
]

app_name = "taxi"
