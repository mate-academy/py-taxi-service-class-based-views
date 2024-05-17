from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("manufacturers/", views.ManufacturerListView.as_view(), name="manufacturers"),
    path("cars/", views.CarListView.as_view(), name="cars"),
    path("cars/<int:pk>/", views.CarDetailView.as_view(), name="car-detail"),
    path("drivers/", views.DriverListView.as_view(), name="drivers"),
    path("drivers/<int:pk>", views.DriverDetailView.as_view(), name="driver-detail"),
]

app_name = "taxi"
