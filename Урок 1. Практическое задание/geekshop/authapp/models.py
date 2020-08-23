from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class ShopUser(AbstractUser):
    SEX_MALE = 'male'
    SEX_FEMALE = 'female'
    SEX_OTHER = 'other'

    SEX_CHOICE = (
        (SEX_MALE, 'Мужской'),
        (SEX_FEMALE, 'Женский'),
        (SEX_OTHER, 'Не указан'),
    )

    avatar = models.ImageField(upload_to='users_avatars', blank=True)   # аватарка
    age = models.PositiveIntegerField(verbose_name='возраст')           # возраст
    sex = models.CharField(max_length=6, choices=SEX_CHOICE, default=SEX_OTHER, verbose_name='Пол')  # male, female

    activation_key = models.CharField(max_length=128, blank=True)   # код для активации
    # поле для указания, когда истечет срок действия ключа. Срок действия ключа
    # 48 часов от момента создания учетной записи
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    # Срок действия ключа активации истек?
    def is_activation_key_expired(self):
        """Выполняет проверку актуальности ключа"""
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
