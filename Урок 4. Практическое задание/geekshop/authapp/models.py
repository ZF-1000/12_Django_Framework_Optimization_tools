from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
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

    avatar = models.ImageField(upload_to='users_avatars', blank=True)       # аватарка
    # так как ВКонтакте API не передает в ответе возраст пользователя, пропишем default=18
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)   # возраст
    sex = models.CharField(max_length=6, choices=SEX_CHOICE, default=SEX_OTHER, verbose_name='Пол')  # male, female

    activation_key = models.CharField(max_length=128, blank=True)   # код для активации
    # поле для указания, когда истечет срок действия ключа. Срок действия ключа
    # 48 часов от момента создания учетной записи
    activation_key_expires = models.DateTimeField(
        verbose_name='актульность ключа',
        default=(now() + timedelta(hours=48))
    )

    # Срок действия ключа активации истек?
    def is_activation_key_expired(self):
        """Выполняет проверку актуальности ключа"""
        if now() <= self.activation_key_expires:
            return False
        else:
            return True


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )
    # OneToOneField - создания связи «один-к-одному»
    # db_index=True - для данного поля создается индекс
    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    # choices=GENDER_CHOICES
    # получаем фиксированный набор значений, которые прописаны в кортеже GENDER_CHOICES,
    # содержащем кортежи из пар «значение в БД» – «отображаемое значение»
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    # @receiver - декоратор, который при получении определенных сигналов вызывает
    # задекорированный метод. При работе со связью «один-к-одному» необходим механизм синхронных
    # действий со связанной моделью
    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        """Создание профиля"""
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        """Сохранение профиля"""
        instance.shopuserprofile.save()
