import datetime

from django_celery_beat.models import PeriodicTask, IntervalSchedule

from celery import shared_task

from habit.models import Habit
from users.services import MyBot


@shared_task
def get_data_for_message_habit():
    """Функция получения данных для отправки сообщений пользователям о необходимости выполнить привычку"""
    habits = Habit.objects.all()
    date_now = datetime.datetime.now().date()
    time_now = datetime.datetime.now().time()

    for habit in habits:
        if habit.date_habit == date_now:
            if habit.time < time_now and habit.pleasant_habit is False:
                user_telegram = habit.user.telegram
                message = f'Пришло время {habit.action} в {habit.place}'
                habit.date_habit = date_now
                habit.save()
                MyBot().send_message(user_telegram, message)

                # Создаем интервал для повтора
                schedule, created = IntervalSchedule.objects.get_or_create(
                    every=habit.periodicity,
                    period=IntervalSchedule.DAYS,
                )

                # Создаем задачу для повторения
                PeriodicTask.objects.create(
                    interval=schedule,
                    name=f'{habit.action}',
                    task='habit.tasks.get_data_for_message_habit',
                    args=[habit.id],
                    start_time=habit.time)

