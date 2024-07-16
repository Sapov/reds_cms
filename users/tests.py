from django.http import HttpRequest
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from users.views import Register, dashboard


class LoginPageTests(TestCase):
    def setUp(self):
        url = reverse('login')
        self.response = self.client.get(url)

    def test_login_page(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_loginpage(self):
        'шаблона'
        self.assertTemplateUsed(self.response, 'registration/login.html')
        self.assertContains(self.response, 'Login')

    def test_signup_view(self):  # new
        "Проверяем что вызывается функция"
        view = resolve('/users/login/')

        self.assertEqual(view.func.__name__,
                         Register.as_view().__name__)

    # def test_dashbord_page_returns_correct_code(self):
    #     requests = HttpRequest()
    #     response = dashboard(requests)
    #     self.assertEqual(self.response.status_code, 200)
