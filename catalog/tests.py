from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def setUp(self):
        super().setUp()
        self.response = self.client.get(reverse("home"))

    def test_returns_rental_ops(self):
        self.assertContains(
            response=self.response, text="<h1>RentalOps</h1>", html=True
        )

    def test_uses_correct_template(self):
        self.assertTemplateUsed(self.response, template_name="catalog/home.html")

    def test_has_correct_title(self):
        self.assertContains(self.response, text="<title>RentalOps</title>", html=True)
