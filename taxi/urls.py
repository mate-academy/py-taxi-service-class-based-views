from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    ManufacturerListView,
    DriverListView,
    DriverDetailView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list"
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "taxi"
