from django.db import models

# Create your models here.

class Product(models.Model):

    CATEGORY_CHOICES = (
        ('currency', 'Внутриигровая валюта'),
        ('item', 'Игровой предмет'),
        ('account', 'Игровой аккаунт'),
        ('service', 'Услуга'),
        ('other', 'Другое'),
    )

    STATUS_CHOICE = (
        ('active', 'Активный'),
        ('sold', 'Проданный'),
        ('deleted', 'Удаленный'),
    )

    seller = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE, related_name='products', verbose_name="Продавец")
    name = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField (blank=True, default='', verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, verbose_name='Категория')
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='active', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обнавления')
    count = models.PositiveIntegerField(default=1, verbose_name="Количество")


    def __str__(self):
        return f'{self.name}: {self.price} РУБ. ({self.seller})'
