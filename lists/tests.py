from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)

    def test_resolve_root_url_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
