from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Класс для создания модели пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='почта пользователя')
    telegram = models.CharField(max_length=200, null=True, blank=True, verbose_name='телеграм пользователя')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

