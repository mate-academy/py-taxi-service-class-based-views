from django.urls import path

from taxi.views import (
    CarDetailView,
    CarsLlistView,
    DriverDetailView,
    DriversListView,
    HomePageView,
    manufacturer_detail_view,
    manufacturers_list_view,
)

app_name = "taxi"
urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("manufacturers/", manufacturers_list_view, name="manufacturer-list"),
    path("cars/", CarsLlistView.as_view(), name="car-list"),
    path("drivers/", DriversListView.as_view(), name="driver-list"),
    path(
        "manufacturers/<int:pk>/",
        manufacturer_detail_view,
        name="manufacturer-detail"
    ),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
]
