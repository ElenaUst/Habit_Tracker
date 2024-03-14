from rest_framework import serializers

from habit.models import Habit
from habit.validators import time_limit, periodicity_limit, HabitValidate


class HabitSerializer(serializers.ModelSerializer):
    """Класс сериализатора для привычки"""
    time_to_complete = serializers.IntegerField(validators=[time_limit])
    periodicity = serializers.IntegerField(validators=[periodicity_limit])

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitValidate(pleasant_habit='pleasant_habit', related_habit='related_habit', reward='reward')]
