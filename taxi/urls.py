from django.urls import path

from .views import index, ManufacturerListView, CarListView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer_list_view"),
    path("cars/", CarListView.as_view(), name="cars_list_view"),
]

app_name = "taxi"
