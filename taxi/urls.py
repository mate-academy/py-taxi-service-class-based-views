from django.urls import path

from .views import index, ManufacturerListView, CarListView
from .views import CarDetailView, DriverListView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/",
         ManufacturerListView.as_view(),
         name="manufacturers"),
    path("car/", CarListView.as_view(), name="cars"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="cars-detail"),
    path("driver/", DriverListView.as_view(), name="drivers"),
    path("driver/<int:pk>/", DriverDetailView.as_view(), name="drivers-detail")
]

app_name = "taxi"
