import datetime

from django.db import models

from users.models import User


class Habit(models.Model):
    """Класс для создания модели привычки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель привычки', blank=True, null=True)
    place = models.CharField(max_length=250, verbose_name='место выполнения привычки', blank=True, null=True)
    time = models.TimeField(verbose_name='время выполнения', blank=True, null=True)
    action = models.CharField(max_length=500, verbose_name='выполняемое действие')
    pleasant_habit = models.BooleanField(verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', blank=True,
                                      null=True)
    periodicity = models.IntegerField(verbose_name='периодичность выполнения привычки')
    reward = models.CharField(max_length=150, verbose_name='вознаграждение', blank=True, null=True)
    time_to_complete = models.IntegerField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности привычки')
    date_habit = models.DateField(default=datetime.date.today(), verbose_name='дата последнего выполнения привычки', blank=True, null=True)

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ['action']
