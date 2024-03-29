from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page


class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)

    def test_resolve_root_url_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('To-Do', html)
        self.assertTrue(html.endswith('</html>'))
