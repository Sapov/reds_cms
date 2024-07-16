from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

        self.browser.get("http://127.0.0.1:8000/")

    def test_page_login(self):
        '''Проверка наличия страницы "Вход"'''
        self.assertIn('Сервис онлайн печати баннеров', self.browser.title)

    def tearDown(self):
        self.browser.quit()

    # def test_new_visitor_can_sign_up(self):
    #     self.browser.find_element_by_id("id_username").send_keys("test")
    #     self.browser.find_element_by_id("id_email").send_keys("test@test.com")
    #     self.browser.find_element_by_id("id_password1").send_keys("test")
    #     self.browser.find_element_by_id("id_password2").send_keys("test")
    #     self.browser.find_element_by_id("id_submit").click()


if __name__ == '__main__':
    unittest.main(warnings='ignore')