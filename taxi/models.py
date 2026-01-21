from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Manufacturer name",
        help_text="Official manufacturer name",
    )
    country = models.CharField(
        max_length=63,
        verbose_name="Country",
        help_text="Country where the manufacturer is based",
    )

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["country"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "country"],
                name="unique_manufacturer_per_country",
            )
        ]

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="License number",
        help_text="Format: ABC12345",
        validators=[
            RegexValidator(
                regex=r"^[A-Z]{3}\d{5}$",
                message="Format: ABC12345",
            )
        ],
    )

    class Meta:
        ordering = ["username"]

    def save(self, *args, **kwargs):
        if self.license_number:
            self.license_number = self.license_number.upper()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.username


class Car(models.Model):
    model = models.CharField(
        max_length=100,
        verbose_name="Car model",
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
        verbose_name="Manufacturer",
    )
    drivers = models.ManyToManyField(
        Driver,
        related_name="cars",
        verbose_name="Assigned drivers",
        blank=True,
    )

    class Meta:
        ordering = ["manufacturer__name", "model"]
        constraints = [
            models.UniqueConstraint(
                fields=["manufacturer", "model"],
                name="unique_car_per_manufacturer",
            )
        ]

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"
