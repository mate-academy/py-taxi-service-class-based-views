from xml.etree.ElementInclude import include

from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls

from taxi.views import (index,
                        ManufacturerListView,
                        CarListView, DriverListView,
                        cardetailview,
                        DriverDetailView)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturer/", ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("car/", CarListView.as_view(), name="car-list"),
    path("car/<int:pk>/", cardetailview, name="car-detail"),
    path("driver/", DriverListView.as_view(), name="driver-list"),
    path("driver/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"),
]
app_name = "taxi"
