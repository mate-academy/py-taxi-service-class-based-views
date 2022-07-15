from django.urls import path

from .views import index, ManufacturerListView, CarListView, CarDetailView, DriverListView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("cars/", CarListView.as_view(), name="cars_list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car_detailed"),
    path("drivers/", DriverListView.as_view(), name="drivers_list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="driver_detailed"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturers_list"),

]

app_name = "taxi"
