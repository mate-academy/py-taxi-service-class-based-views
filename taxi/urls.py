from django.urls import path

from .views import index, ManufacturersListView, CarListView
from .views import CarDetailView, DriverListView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/",
         ManufacturersListView.as_view(),
         name="manufacturers-list"),
    path("cars/",
         CarListView.as_view(),
         name="cars-list"),
    path("cars/<int:pk>/",
         CarDetailView.as_view(),
         name="cars-detail-view"
         ),
    path("drivers/",
         DriverListView.as_view(),
         name="drivers-list"),
    path("drivers/<int:pk>/",
         DriverDetailView.as_view(),
         name="drivers-detail-view")
]

app_name = "taxi"
