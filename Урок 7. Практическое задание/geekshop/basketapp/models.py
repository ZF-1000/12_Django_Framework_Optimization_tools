from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings
from mainapp.models import Product
from django.utils.functional import cached_property


class BasketQuerySet (models.QuerySet):
    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super(BasketQuerySet, self).delete(*args, **kwargs)


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket', verbose_name='Пользователь',)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт',)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество',)
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')

    @property
    def get_product_cost(self):
        return self.product.price * self.quantity

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()

    @property
    def get_total_quantity(self):
        items = self.get_items_cached
        # items = Basket.objects.filter(user=self.user)
        total_items_count = sum(list(map(lambda x: x.quantity, items)))
        return total_items_count

    @property
    def get_total_cost(self):
        items = self.get_items_cached
        # items = Basket.objects.filter(user=self.user)
        total_items_cost = sum(list(map(lambda x: x.get_product_cost, items)))
        return total_items_cost

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by('product__category')

    @staticmethod
    def get_product(user, product):
        return Basket.objects.filter(user=user, product=product)

    @staticmethod
    def get_products_quantity(cls, user):
        basket_items = cls.get_items(user)
        basket_items_dic = {}
        [basket_items_dic.update({item.product: item.quantity}) for item in basket_items]

        return basket_items_dic

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    # переопределяем метод, сохранения объекта
    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity

        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args, **kwargs)

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super(self.__class__, self).delete()
