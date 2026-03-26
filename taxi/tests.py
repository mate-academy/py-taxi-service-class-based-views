from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Driver

class TaxiServiceAuthTests(TestCase):
    def setUp(self):
        # создаем пользователя и водителя
        self.user = User.objects.create_user(username='admin.user', password='1qazcde3')
        self.driver = Driver.objects.create(user=self.user, license_number='ABC123')

    def test_home_redirect_for_anonymous(self):
        """Проверяем редирект неавторизованного пользователя с /"""
        response = self.client.get(reverse('taxi:index'))
        self.assertRedirects(response, f'/login/?next={reverse("taxi:index")}')

    def test_home_access_authenticated(self):
        self.client.login(username='admin.user', password='1qazcde3')
        response = self.client.get(reverse('taxi:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You visited this page")

    def test_visit_counter_increment(self):
        self.client.login(username='admin.user', password='1qazcde3')
        self.client.get(reverse('taxi:index'))
        response = self.client.get(reverse('taxi:index'))
        self.assertContains(response, "You visited this page 1 times")  # первый визит = 0, второй = 1

    def test_driver_list_me(self):
        self.client.login(username='admin.user', password='1qazcde3')
        response = self.client.get(reverse('taxi:driver-list'))
        self.assertContains(response, "admin.user (Me)")

    def test_login_view(self):
        response = self.client.get(reverse('taxi:login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<form")

    def test_logout_view_redirect(self):
        self.client.login(username='admin.user', password='1qazcde3')
        response = self.client.get(reverse('taxi:logout'))
        self.assertRedirects(response, '/login/')