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
        'шаблон Логина'
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


class RegisterPageTests(TestCase):
    def setUp(self):
        url = reverse('register')
        self.response = self.client.get(url)

    def test_register_page(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_register(self):
        'шаблон register'
        self.assertTemplateUsed(self.response, 'registration/register.html')
        self.assertContains(self.response, 'register')

    def test_signup_view(self):  # new
        "Проверяем что вызывается функция"
        view = resolve('/users/register/')

        self.assertEqual(view.func.__name__,
                         Register.as_view().__name__)


class ConfirmEmailPageTests(TestCase):
    def setUp(self):
        url = reverse('confirm_email')
        self.response = self.client.get(url)

    def test_register_page(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_register(self):
        'шаблон confirm_email'
        self.assertTemplateUsed(self.response, 'registration/confirm_email.html')
        self.assertContains(self.response, 'Пожалуйста, проверьте свою почту, чтобы завершить регистрацию... ')

    def test_signup_view(self):  # new
        "Проверяем что вызывается функция"
        view = resolve('/users/confirm_email/')

        self.assertEqual(view.func.__name__,
                         Register.as_view().__name__)


class InvalidVerifyPageTests(TestCase):
    def setUp(self):
        url = reverse('invalid_verify')
        self.response = self.client.get(url)

    def test_register_page(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_register(self):
        'шаблон invalid_verify'
        self.assertTemplateUsed(self.response, 'registration/invalid_verify.html')
        self.assertContains(self.response, 'Ваша ссылка не корректна, залогиньтесь снова')

    def test_signup_view(self):  # new
        "Проверяем что вызывается функция"
        view = resolve('/users/invalid_verify/')

        self.assertEqual(view.func.__name__,
                         Register.as_view().__name__)

# нужна авторизация
# class UserListTests(TestCase):
#     def setUp(self):
#         url = reverse('user_list')
#         self.response = self.client.get(url)
#
#     def test_login_page(self):
#         self.assertEqual(self.response.status_code, 200)
#
#     def test_template_loginpage(self):
#         'шаблон user_list'
#         self.assertTemplateUsed(self.response, 'users/user_list.html')
#         self.assertContains(self.response, 'Пользователи:')
#
#     def test_signup_view(self):  # new
#         "Проверяем что вызывается функция"
#         view = resolve('/users/list_user/')
#
#         self.assertEqual(view.func.__name__,
#                          Register.as_view().__name__)
