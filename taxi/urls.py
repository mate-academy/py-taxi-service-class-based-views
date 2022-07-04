from django.urls import path

from .views import index, ManufacturerListView, CarsListView, CarsDetailedListView, DriversListView, DriversDetailedListView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(), name="Manufacturer-List"),
    path("cars/", CarsListView.as_view(), name="Car-List"),
    path("cars/<int:pk>/", CarsDetailedListView.as_view(), name="cars_datailed_view"),
    path("drivers/<int:pk>/", DriversDetailedListView.as_view(), name="drivers_detailed_view"),
    path("drivers", DriversListView.as_view(), name="Driver-List")
]

app_name = "taxi"
