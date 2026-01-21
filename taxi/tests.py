from django.test import TestCase
from taxi.models import Manufacturer, Driver


class ManufacturerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Manufacturer.objects.create(name="Lincoln", country="USA")
        Manufacturer.objects.create(name="Ford Motor Company", country="USA")
        Manufacturer.objects.create(name="Toyota", country="Japan")

    def test_manufacturer_creation(self):
        manufacturer = Manufacturer.objects.get(name="Lincoln")
        self.assertEqual(manufacturer.country, "USA")

    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.get(name="Ford Motor Company")
        self.assertEqual(str(manufacturer), "Ford Motor Company")


class DriverModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create sample drivers
        Driver.objects.create(
            username="admin.user",
            first_name="Admin",
            last_name="User",
            email="admin.user@taxi.com",
            password="pbkdf2_sha256$320000$6uM28XWOFX6ewyloJzjqmt$L",
            license_number="ADM56984",
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        Driver.objects.create(
            username="joyce.byers",
            first_name="Joyce",
            last_name="Byers",
            email="joyce.byers@taxi.com",
            password="pbkdf2_sha256$320000$73Z1Y57bcoscZ37s9rE9v0$4SEQ0",
            license_number="JOY26458",
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

    def test_driver_creation(self):
        driver = Driver.objects.get(username="admin.user")
        self.assertEqual(driver.first_name, "Admin")
        self.assertEqual(driver.is_active, True)

    def test_driver_str(self):
        driver = Driver.objects.get(username="joyce.byers")
        self.assertEqual(str(driver), "Joyce Byers")
