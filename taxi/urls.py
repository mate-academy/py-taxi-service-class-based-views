from django.template import Template
from django.urls import path
from django.views.generic import TemplateView

from .views import index, CarDetailView, DriverDetailView, ManufacturerListView, CarListView, DriverListView

urlpatterns = [
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer-list"),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"),
]

app_name = "taxi"
