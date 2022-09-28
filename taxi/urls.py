from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import index, \
    ManufacturerListView, \
    CarListView, \
    CarDetailView, DriverDetailView, DriverListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer_list"
    ),
    path(
        "cars/",
        CarListView.as_view(),
        name="car_list"
    ),
    path(
        "cars/<int:pk>/",
        CarDetailView.as_view(),
        name="car_detail"
    ),
    path(
        "drivers/",
        DriverListView.as_view(),
        name="driver_list"
    ),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver_detail"
    )
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "taxi"
