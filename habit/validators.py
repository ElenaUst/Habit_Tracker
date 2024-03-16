from rest_framework import serializers
from rest_framework.exceptions import ValidationError


def time_limit(value):
    """Функция валидации максимального времени выполнения привычки"""
    if value > 120:
        raise serializers.ValidationError('Время выполнения привычки не должно превышать 120 секунд')


def periodicity_limit(value):
    """Функция валидации максимальной периодичности привычки"""
    if value > 7:
        raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')


class HabitValidate:
    """Класс для валидации привычки"""

    def __init__(self, pleasant_habit, related_habit, reward):
        self.pleasant_habit = pleasant_habit
        self. related_habit = related_habit
        self.reward = reward

    def __call__(self, value):
        pleasant_habit = value.get(self.pleasant_habit)
        related_habit = value.get(self.related_habit)
        reward = value.get(self.reward)

        if related_habit and reward:
            raise ValidationError('Нельзя одновременно выбрать связанную привычку и вознаграждение')

        if related_habit and not pleasant_habit:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки')

        if pleasant_habit and (related_habit or reward):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')

        if not (pleasant_habit, reward):
            raise ValidationError('У полезной привычки необходимо указать вознаграждение или приятную привычку')