from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("license_number",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "license_number",
                    )
                },
            ),
        )
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)
    list_display = ("model", "manufacturer", "drivers_list_display")

    def drivers_list_display(self, obj):
        drivers = [str(driver) for driver in obj.drivers.all()]
        return ", ".join(drivers)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related("drivers")

    drivers_list_display.short_description = "Drivers"


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
