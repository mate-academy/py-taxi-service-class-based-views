from django.urls import path

from .views import index, ManufacturerListView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturer/", ManufacturerListView.as_view(), name="manufacturer_list_view")
]

app_name = "taxi"
