from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket', verbose_name='Пользователь',)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт',)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество',)
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        items = Basket.objects.filter(user=self.user)
        total_items_count = sum(list(map(lambda x: x.quantity, items)))
        return total_items_count

    @property
    def total_cost(self):
        items = Basket.objects.filter(user=self.user)
        total_items_cost = sum(list(map(lambda x: x.product_cost, items)))
        return total_items_cost
