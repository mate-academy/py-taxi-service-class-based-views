from django.urls import path

from . import views

app_name = "taxi"

urlpatterns = [
    path("", views.index, name="index"),

    path("manufacturers/", views.ManufacturerListView.as_view(), name="manufacturer-list"),
    path("cars/", views.CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", views.CarDetailView.as_view(), name="car-detail"),
    path("drivers/", views.DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>/", views.DriverDetailView.as_view(), name="driver-detail"),
]
