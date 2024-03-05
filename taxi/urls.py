from django.urls import path

from taxi.views import index
from taxi.views import ManufacturerListView
from taxi.views import CarListView
from taxi.views import CarDetailView
from taxi.views import DriverListView
from taxi.views import DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/",
         ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>/",
         DriverDetailView.as_view(),
         name="driver-detail"),

]

app_name = "taxi"
