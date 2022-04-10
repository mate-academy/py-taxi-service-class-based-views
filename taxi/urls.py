from django.urls import path

from .views import (
    index,
    ManufacturerListView,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path('manufacturers/', ManufacturerListView.as_view()),
    path('cars/', CarListView.as_view()),
    path('cars/<int:pk>/', CarDetailView.as_view()),
    path('drivers/', DriverListView.as_view()),
    path('drivers/<int:pk>/', DriverDetailView.as_view())
]

app_name = "taxi"
