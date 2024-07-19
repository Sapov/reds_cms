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
