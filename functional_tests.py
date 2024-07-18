from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

from selenium.webdriver.support.select import Select


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
        # Добавляем новый адрес доставки
        self.browser.get("http://127.0.0.1:8000/users/list_address/")
        self.browser.find_element(By.CSS_SELECTOR, "[class='text']").click()
        time.sleep(2)
        self.browser.find_element(By.CSS_SELECTOR, "[name='region']").send_keys("Московская область")
        self.browser.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Краснознаменск")
        self.browser.find_element(By.CSS_SELECTOR, "[name='street']").send_keys("Ленина")
        self.browser.find_element(By.CSS_SELECTOR, "[name='house']").send_keys("66")
        self.browser.find_element(By.CSS_SELECTOR, "[name='floor']").send_keys("1")
        self.browser.find_element(By.CSS_SELECTOR, "[name='flat']").send_keys("97")
        self.browser.find_element(By.CSS_SELECTOR, "[name='first_name']").send_keys("Юрий")
        self.browser.find_element(By.CSS_SELECTOR, "[name='second_name']").send_keys("Борисович")
        self.browser.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7984455175")
        select = Select(self.browser.find_element(By.CSS_SELECTOR, "[name='delivery_method']"))
        select.select_by_value('1')
        time.sleep(3)
        self.browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        time.sleep(3)

    # def test_login_page_1(self):
    #     'Тестирую CRUD операций с адресами, которые можно создать и изменить'
    #     self.browser.get("http://127.0.0.1:8000/users/list_address/")
    #     self.browser.find_element(By.CSS_SELECTOR, "[class='text']").click()
    #     time.sleep(2)


    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
