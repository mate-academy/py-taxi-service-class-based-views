from django.urls import path

from taxi.views import (
    CarDetailView,
    CarsLlistView,
    DriverDetailView,
    DriversListView,
    home_page,
    manufacturer_detail_view,
    manufacturers_list_view,
)

app_name = "taxi"
urlpatterns = [
    path("", home_page, name="index"),
    path("manufacturers/", manufacturers_list_view, name="manufacturer-list"),
    path("cars/", CarsLlistView.as_view(), name="car-list"),
    path("drivers/", DriversListView.as_view(), name="driver-list"),
    path("manufacturers/<int:pk>/", manufacturer_detail_view, name="manufacturer-detail"),  # noqa: E501
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"),  # noqa: E501
]
