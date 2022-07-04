from django.urls import path

from .views import index, ManufacturerListView, CarListView, CarDetailView, DriverDetailView, DriverListView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(template_name='taxi/manufacturer_list.html'),
         name='manufacturers'),
    path("cars/", CarListView.as_view(template_name='taxi/car_list.html'),
         name='cars'),
    path("drivers/", DriverListView.as_view(template_name='taxi/driver_list.html'),
         name='drivers'),
    path("cars/<int:pk>/", CarDetailView.as_view(template_name='taxi/car_detail.html'),
         name='car_detail'),
    path("driver/<int:pk>/", DriverDetailView.as_view(template_name='taxi/driver_detail.html'),
         name='driver_detail'),
]

app_name = "taxi"
