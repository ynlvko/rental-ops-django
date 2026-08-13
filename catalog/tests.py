from django.test import Client, SimpleTestCase, TestCase

# Create your tests here.
class CatalogTests(SimpleTestCase):
    def test_root_answers(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'RentalOps')
