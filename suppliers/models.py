from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=20, verbose_name="Номер дома")
    products = models.ManyToManyField('Product', blank=True, verbose_name="Продукты")
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sub_suppliers',
        verbose_name="Поставщик"
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name="Задолженность"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        ordering = ["-pk",]

    def __str__(self):
        return self.name

    def get_level(self):
        level = 0
        current = self
        while current.supplier:
            level += 1
            current = current.supplier
        return level


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["-pk", ]
        indexes = [
            models.Index(fields=["-pk"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.model})"
