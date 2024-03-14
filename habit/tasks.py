import datetime

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
        if date_now == habit.date + habit.periodicity:
            if time_now == habit.time and habit.pleasant_habit == 'False':
                user_telegram = Habit.user.telegram
                message = f'Пришло время {habit.action} в {habit.place}'
                habit.date = date_now
                habit.save()
                MyBot().send_message(user_telegram, message)
