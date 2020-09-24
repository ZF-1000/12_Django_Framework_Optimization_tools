import os
import json
from django.core.management import BaseCommand

from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser


def load_json(file_name):
    with open(os.path.join('mainapp/json', file_name + '.json'), encoding="utf-8") as json_file:
        return json.load(json_file)  # чтение из потока


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # создание категории
        # ProductCategory.objects.create(
        #     name='Шкафы'
        # )
        # categories = load_json('categories')
        # # print(categories)
        # ProductCategory.objects.all().delete()  # очищаем базу, удаляем категории
        #
        # for cat in categories:
        #     new_cat = ProductCategory(**cat)  # создали новую категорию с параметрами name и description
        #     new_cat.save()  # записали словарь в базу
        #
        # products = load_json('products')
        # Product.objects.all().delete()
        #
        # for product in products:
        #     category_item = ProductCategory.objects.get(name=product['category'])
        #     product['category'] = category_item
        #     new_prod = Product(**product)
        #     new_prod.save()

        # Создаем суперпользователя при помощи менеджера модели
        super_user = ShopUser.objects.create_superuser(
            'django',                   # имя админа
            'django@geekshop.local',    # почта
            'geekbrains',               # пароль
            age=33                      # возраст
        )
