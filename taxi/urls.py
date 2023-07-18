from django.urls import path

from taxi import views

app_name = "taxi"

urlpatterns = [
    path("", views.index, name="index"),
    path("cars/", views.CarListView.as_view(), name="car-list"),
    path("drivers/", views.DriverListView.as_view(), name="driver-list"),

    path("manufacturers/",
         views.ManufacturerListView.as_view(),
         name="manufacturer-list"),

    path("cars/<int:pk>/",
         views.CarDetailedView.as_view(),
         name="car-detail"),

    path("drivers/<int:pk>/",
         views.DriverDetailedView.as_view(),
         name="driver-detail"),
]
