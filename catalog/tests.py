from django.test import Client, SimpleTestCase


class CatalogTests(SimpleTestCase):
    def test_root_answers(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "RentalOps")
