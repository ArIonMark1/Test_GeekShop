import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta, datetime


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст')

    activation_key = models.ImageField(max_length=128, blank=True)
    activation_key_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48))) = not correct

    def is_activation_key_expired(self):  # функция для проверки
        if datetime.now() < self.activation_key_created + timedelta(hours=48):
            return False
        return True
