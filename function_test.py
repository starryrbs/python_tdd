import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Django', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
