import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        # 创建chrome参数对象
        opt = webdriver.ChromeOptions()

        # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
        opt.headless = True
        self.browser = webdriver.Chrome(options=opt)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('To-Do', self.browser.page_source)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
