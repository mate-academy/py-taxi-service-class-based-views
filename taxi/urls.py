from django.urls import path

from .views import index, ManufacturerListView, CarListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturers-list"),
    path(
        "cars/",
        CarListView.as_view(),
        name="car-list"

    )
]

app_name = "taxi"
