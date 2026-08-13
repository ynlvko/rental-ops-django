from django.test import SimpleTestCase
from django.urls import reverse


class HealthCheckTests(SimpleTestCase):
    def test_returns_ok(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ok")


class NotFoundTests(SimpleTestCase):
    def test_404_for_unknown(self):
        response = self.client.get("unknown_route")
        self.assertEqual(response.status_code, 404)
