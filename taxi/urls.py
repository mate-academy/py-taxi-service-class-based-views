from django.urls import path

from .views import index, ManufacturersListView, CarListView, CarDetailView, DriverListView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturersListView.as_view(), name="manufacturers-list"),
    path("cars/", CarListView.as_view(), name="car_list"),
    path("cars/<int:pk>", CarDetailView.as_view(), name="car_detail"),
    path("drivers/", DriverListView.as_view(), name="driver_list"),
    path("drivers/<int:pk>", DriverDetailView.as_view(), name="driver_detail")
]

app_name = "taxi"
