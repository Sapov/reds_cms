from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTests(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.browser = webdriver.Chrome(options=options)

        self.browser.get("http://127.0.0.1:8000/")

    def test_page_login(self):
        '''Проверка наличия страницы "Вход"'''
        self.assertIn('Сервис онлайн печати баннеров', self.browser.title)

    def test_login_page(self):
        self.browser.find_element(By.CSS_SELECTOR, "[name='username']").send_keys("vasa@mail.ru")
        self.browser.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("q911ww1234")
        self.browser.find_element(By.CSS_SELECTOR, "[name='button']").click()
        time.sleep(3)
        self.assertIn('Дашборд', self.browser.title)  # переход в дашборд
        time.sleep(2)

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
