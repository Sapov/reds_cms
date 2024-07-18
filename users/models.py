from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Role(models.TextChoices):
    """Роли пользователей"""

    CUSTOMER_RETAIL = "CUSTOMER_RETAIL", "Клиент"  # розничный клиент
    CUSTOMER_AGENCY = "CUSTOMER_AGENCY", "Рекламное агентство"  # Рекламное агентство
    MANAGER = "MANAGER", "Менеджер"
    OPERATOR = "OPERATOR", "Оператор"
    FINANCIER = "FINANCIER", "Бухгалтер"


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, verbose_name='Телефон')
    role = models.CharField(max_length=24, choices=Role.choices, default=Role.CUSTOMER_RETAIL)
    email = models.EmailField(_("email address"), unique=True, )
    email_verify = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def get_absolute_url(self):
        return reverse('user_list')


class Delivery(models.TextChoices):
    """Типы Доставки"""

    YANDEX = "YANDEX_DELIVERY", "Яндекс-доставка"
    CDEK = "CDEK", "Доставка СДЕК"


class DeliveryAddress(models.Model):
    '''Адреса доставки польлmзователя'''
    Contractor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="ЗАКАЗЧИК",
                                   null=True, blank=True)
    region = models.CharField(max_length=100, verbose_name="Область", null=True, blank=True)
    city = models.CharField(max_length=200, verbose_name="Город", null=True, blank=True)
    street = models.CharField(max_length=200, verbose_name="Улица", null=True, blank=True)
    house = models.CharField(max_length=200, verbose_name="Дом", null=True, blank=True)
    entrance = models.CharField(max_length=10, verbose_name="Подъезд", null=True, blank=True)
    floor = models.CharField(max_length=10, verbose_name="Этаж", null=True, blank=True)
    flat = models.CharField(max_length=10, verbose_name="Квартира/офис", null=True, blank=True)
    first_name = models.CharField(max_length=100, verbose_name="Имя получателя", null=True, blank=True)
    second_name = models.CharField(max_length=100, verbose_name="Фамилия получателя", null=True, blank=True)
    phone = models.CharField(max_length=100, verbose_name="Телефон получателя", null=True, blank=True)
    delivery_method = models.CharField(max_length=36, choices=Delivery.choices, default=Delivery.YANDEX, )

    class Meta:
        verbose_name_plural = "Адреса доставки"
        verbose_name = "Адреса доставки"
        ordering = ["street"]

    def __str__(self):
        return f"{self.delivery_method}-{self.city}-{self.street}-{self.house}"

    def get_absolute_url(self):
        return reverse('address_list')


class Organisation(models.Model):
    Contractor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="ЗАКАЗЧИК",
                                   default=1,
                                   )
    name_ul = models.CharField(
        max_length=70,
        verbose_name="Имя юр. лица",
        help_text="Форма собственности и название.",
        default="ООО Рога и Копыта",
    )
    address_ur = models.TextField(
        null=True,
        blank=True,
        verbose_name="Юр. Адрес",
        help_text="Юридический почтовый адрес",
    )
    address_post = models.TextField(
        null=True, blank=True, verbose_name="Почтовый Адрес"
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    phone2 = models.CharField(
        max_length=20, blank=True, verbose_name="Телефон резервный"
    )
    email = models.EmailField(
        max_length=20, blank=True, verbose_name="Электронная почта"
    )
    inn = models.CharField(max_length=12, verbose_name="ИНН", blank=True)
    kpp = models.CharField(max_length=9, verbose_name="КПП", blank=True)
    okpo = models.CharField(max_length=12, blank=True, verbose_name="ОКПО")
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Опубликовано"
    )

    class Meta:
        verbose_name_plural = "Организации"
        verbose_name = "Организация"
        ordering = ["name_ul"]

    def __str__(self):
        return self.name_ul

    def get_absolute_url(self):
        return reverse('organization_list')
