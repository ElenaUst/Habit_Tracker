import requests
from django.conf import settings


class MyBot:
    """Класс для отправки напоминаний о выполнении привычки в телеграм"""
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_TOKEN

    def send_message(self, user_telegram,  message):

        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={'chat_id': user_telegram,
                  'text': message}
        )


