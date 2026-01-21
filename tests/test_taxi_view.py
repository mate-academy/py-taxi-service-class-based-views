from django.test import TestCase
from django.urls import reverse

from taxi.models import Manufacturer

# Corrected reverse URL names
MANUFACTURER_LIST_URL = reverse("taxi:manufacturer_list")  # Fixed
DRIVER_LIST_URL = reverse("taxi:driver_list")  # Fixed
CAR_LIST_URL = reverse("taxi:car_list")  # Fixed
PAGINATION = 5


class ManufacturerListTest(TestCase):
    fixtures = ["taxi_service_db_data.json"]

    def test_manufacturer_list_response_with_correct_template(self):
        response = self.client.get(MANUFACTURER_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "taxi/manufacturer_list.html")

    def test_manufacturer_list_paginated_correctly(self):
        response = self.client.get(MANUFACTURER_LIST_URL)
        self.assertEqual(len(response.context["manufacturers"]), PAGINATION)  # Fixed

    def test_manufacturer_list_ordered_by_name(self):
        response = self.client.get(MANUFACTURER_LIST_URL)
        man_list = Manufacturer.objects.all().order_by("name")
        manufacturer_context = response.context["manufacturers"]  # Fixed context key

        self.assertEqual(
            list(manufacturer_context),
            list(man_list[: len(manufacturer_context)]),
        )


class CarListTest(TestCase):
    fixtures = ["taxi_service_db_data.json"]

    def test_car_list_response_with_correct_template(self):
        response = self.client.get(CAR_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "taxi/car_list.html")

    def test_car_list_paginated_correctly(self):
        response = self.client.get(CAR_LIST_URL)
        self.assertEqual(len(response.context["cars"]), PAGINATION)  # Fixed

    def test_car_detail_response_with_correct_template(self):
        response = self.client.get(reverse("taxi:car_detail", args=[1]))  # Fixed
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "taxi/car_detail.html")


class DriverListTest(TestCase):
    fixtures = ["taxi_service_db_data.json"]

    def test_driver_list_response_with_correct_template(self):
        response = self.client.get(DRIVER_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "taxi/driver_list.html")

    def test_driver_list_paginated_correctly(self):
        response = self.client.get(DRIVER_LIST_URL)
        self.assertEqual(len(response.context["drivers"]), PAGINATION)  # Fixed

    def test_driver_detail_response_with_correct_template(self):
        response = self.client.get(reverse("taxi:driver_detail", args=[1]))  # Fixed
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "taxi/driver_detail.html")
