from django.db import models


# Create your models here.
class FinishWork(models.Model):
    ''' финищная обработка'''
    work = models.CharField(max_length=255, verbose_name="Финишная обработка")
    price_contractor = models.FloatField(
        max_length=100,
        help_text="Цена за 1 м. погонный",
        verbose_name="Себестоимость работы в руб.",
        blank=True,
        null=True,
        default=None,
    )  # стоимость в закупке
    price = models.FloatField(
        max_length=100,
        help_text="Цена за 1 м. погонный",
        verbose_name="Стоимость работы в руб.",
    )

    price_customer_retail = models.FloatField(
        max_length=100,
        help_text="Цена за 1 м. погонный",
        verbose_name="Стоимость работы розница в руб.",
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(default=True, verbose_name="Активный")

    def __str__(self):
        return self.work

    class Meta:
        verbose_name_plural = "Финишные обработки"
        verbose_name = "Финишная обработка"


class TypePrint(models.Model):
    type_print = models.CharField(max_length=128, verbose_name="Метод печати")
    info_type_print = models.TextField(verbose_name="Описание метода печати")

    class Meta:
        verbose_name_plural = "Типы печати"
        verbose_name = "Тип печати"
        ordering = ["type_print"]

    def __str__(self):
        return self.type_print


class Material(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Введите имя материала для печати",
        verbose_name="Материал для печати",
        blank=True,
        null=True,
        default=None,
    )
    type_print = models.ForeignKey(
        TypePrint,
        on_delete=models.PROTECT,
        verbose_name="Тип печати",
        blank=True,
        null=True,
        default=None,
    )
    price_contractor = models.FloatField(
        max_length=100,
        help_text="За 1 м2",
        verbose_name="Себестоимость печати в руб.",
        blank=True,
        null=True,
        default=None,
    )  # стоимость в закупке
    price = models.FloatField(
        max_length=100,
        help_text="За 1 м2",
        verbose_name="Стоимость печати для РА в руб.",
    )
    price_customer_retail = models.FloatField(
        max_length=100,
        help_text="За 1 м2",
        verbose_name="Стоимость печати розница в руб.",
        null=True,
        blank=True,
    )
    resolution_print = models.IntegerField(
        help_text="разрешение для печати на материале",
        verbose_name="DPI",
        blank=True,
        null=True,
        default=None,
    )
    is_active = models.BooleanField(default=True, verbose_name="Активный ")

    def __str__(self):
        return f"{self.name} {self.type_print}"

    class Meta:
        verbose_name_plural = "Материалы для печати"
        verbose_name = "Материал"
        ordering = ["name"]
