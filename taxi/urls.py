from django.urls import path

from .views import index, ManufacturerListView, CarListView, CarDetailView, DriverListView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturers"),
    path("cars/", CarListView.as_view(), name="cars"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="cars_pk"),
    path("drivers/", DriverListView.as_view(), name="drivers"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="drivers_pk"),
]

app_name = "taxi"
