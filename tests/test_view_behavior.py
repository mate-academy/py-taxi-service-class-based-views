from django.test import TestCase
from django.urls import reverse

from taxi.models import Car, Driver, Manufacturer


class ViewBehaviorTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.manufacturer = Manufacturer.objects.create(
            name="Example Motors", country="Example Country"
        )
        cls.driver = Driver.objects.create_user(
            username="example.driver", license_number="ABC12345"
        )
        cls.cars = [
            Car.objects.create(
                model=f"Model {number}", manufacturer=cls.manufacturer
            )
            for number in range(7)
        ]
        cls.driver.cars.add(*cls.cars)

    def test_car_list_has_constant_query_count_and_detail_links(self):
        with self.assertNumQueries(2):
            response = self.client.get(reverse("taxi:car-list"))
        self.assertContains(response, self.manufacturer.name, count=5)
        for car in self.cars[:5]:
            self.assertContains(
                response, reverse("taxi:car-detail", args=[car.pk])
            )

    def test_driver_detail_fetches_all_cars_and_manufacturers_in_two_queries(self):
        with self.assertNumQueries(2):
            response = self.client.get(
                reverse("taxi:driver-detail", args=[self.driver.pk])
            )
        for car in self.cars:
            self.assertContains(response, car.model)
        self.assertContains(response, self.manufacturer.name, count=7)
        self.assertContains(response, self.manufacturer.country, count=7)

    def test_car_detail_displays_manufacturer_and_assigned_driver(self):
        response = self.client.get(
            reverse("taxi:car-detail", args=[self.cars[0].pk])
        )
        for value in (
            self.manufacturer.name,
            self.manufacturer.country,
            self.driver.username,
            self.driver.license_number,
        ):
            self.assertContains(response, value)

    def test_pagination_second_page_and_navigation(self):
        response = self.client.get(reverse("taxi:car-list"))
        self.assertContains(response, 'href="?page=2"')
        self.assertNotContains(response, ">Previous</a>")
        response = self.client.get(reverse("taxi:car-list"), {"page": 2})
        self.assertEqual(list(response.context["car_list"]), self.cars[5:])
        self.assertContains(response, 'href="?page=1"')
        self.assertNotContains(response, ">Next</a>")

    def test_invalid_pages_and_missing_details_return_404(self):
        for page in (0, 100, "invalid"):
            with self.subTest(page=page):
                self.assertEqual(
                    self.client.get(
                        reverse("taxi:car-list"), {"page": page}
                    ).status_code,
                    404,
                )
        for view in ("car-detail", "driver-detail"):
            with self.subTest(view=view):
                self.assertEqual(
                    self.client.get(
                        reverse(f"taxi:{view}", args=[999999])
                    ).status_code,
                    404,
                )

    def test_empty_relationships(self):
        self.driver.cars.clear()
        response = self.client.get(
            reverse("taxi:driver-detail", args=[self.driver.pk])
        )
        self.assertContains(response, "No cars assigned.")
        response = self.client.get(
            reverse("taxi:car-detail", args=[self.cars[0].pk])
        )
        self.assertContains(response, "No drivers assigned.")

    def test_empty_lists(self):
        Car.objects.all().delete()
        Driver.objects.all().delete()
        Manufacturer.objects.all().delete()
        for entity in ("manufacturer", "car", "driver"):
            with self.subTest(entity=entity):
                response = self.client.get(reverse(f"taxi:{entity}-list"))
                self.assertContains(response, f"No {entity}s available.")
                self.assertNotContains(response, 'aria-label="Page navigation"')

    def test_sidebar_links_and_driver_detail_link(self):
        response = self.client.get(reverse("taxi:driver-list"))
        for view in ("index", "manufacturer-list", "car-list", "driver-list"):
            self.assertContains(response, f'href="{reverse(f"taxi:{view}")}"')
        self.assertContains(
            response, reverse("taxi:driver-detail", args=[self.driver.pk])
        )
