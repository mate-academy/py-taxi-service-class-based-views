from django.urls import path

from .views import index, CarListView, DriverListView, ManufacturerListView, CarDetailView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("cars/", CarListView.as_view(), name="cars"),
    path("drivers/", DriverListView.as_view(), name="drivers"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturers"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="cars"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="drivers"),
]

app_name = "taxi"
