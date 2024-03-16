from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование CRUD для привычки"""

    def setUp(self) -> None:
        self.client = APIClient()
        # Создание тестового пользователя
        self.user = User.objects.create(
            email="test@test.com",
            password="test",
        )
        # Аутентификация тестового пользователя
        self.client.force_authenticate(user=self.user)

        # Создание тестовой привычки
        self.habit = Habit.objects.create(
            place="house",
            time="15:00:00",
            action="make homework",
            pleasant_habit="False",
            periodicity=1,
            reward="eat cake",
            is_public=False,
            time_to_complete=120,
            user=self.user,
        )

    def test_habit_create(self):
        """Тестирование создания привычки"""
        # Данные для создания тестовой привычки
        data = {
            "place": "house",
            "time": "16:00:00",
            "action": "make homework",
            "pleasant_habit": False,
            "is_public": False,
            "periodicity": 1,
            "reward": "sleep",
            "time_to_complete": 120

            }
        # Создание привычки
        response = self.client.post('/create/', data=data)

        # Проверка статуса
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Проверка создания привычки
        self.assertEqual(
            response.json(),

            {'id': 2,
             "date": None,
             "place": "house",
             "time": "16:00:00",
             "action": "make homework",
             "pleasant_habit": False,
             "related_habit": None,
             'is_public': False,
             "periodicity": 1,
             "reward": "sleep",
             "time_to_complete": 120,
             "user": self.user.pk}
        )
        # Проверка наличия записи в БД
        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_habit_list(self):
        """Тестирование получения списка привычек"""
        # Создание тестовой привычки
        habit = Habit.objects.create(
            place="house",
            time="16:00:00",
            action="make homework",
            pleasant_habit=False,
            periodicity=1,
            reward="eat cake",
            is_public=True,
            time_to_complete=120,
            user=self.user,
        )
        # Просмотр списка привычек
        response = self.client.get(reverse('habit:habit-list'))

        # Проверка статуса
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        # Проверка вывода списка привычек
        self.assertEqual(
            response.json(),
            {"count": 1,
             "next": None,
             "previous": None,
             "results": [
                 {'id': habit.pk,
                     "date": None,
                     "place": "house",
                     "time": "16:00:00",
                     "action": "make homework",
                     "pleasant_habit": False,
                     "related_habit": None,
                     'is_public': True,
                     "periodicity": 1,
                     "reward": "eat cake",
                     "time_to_complete": 120,
                     "user": self.user.pk}]}
        )

    def test_habit_retrieve(self):
        """Тестирование просмотра привычки"""
        # Создание тестовой привычки
        habit = Habit.objects.create(
                place="house",
                time="16:00:00",
                action="make homework",
                pleasant_habit=False,
                periodicity=1,
                reward="eat cake",
                is_public=True,
                time_to_complete=120,
                user=self.user

            )
        # Просмотр привычки
        response = self.client.get(reverse('habit:habit-detail', args=[habit.pk]))

        # Проверка статуса
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        # Проверка вывода одной привычки
        self.assertEqual(
            response.json(),
            {'id': habit.pk,
             "date": None,
             "place": "house",
             "time": "16:00:00",
             "action": "make homework",
             "pleasant_habit": False,
             "related_habit": None,
             'is_public': True,
             "periodicity": 1,
             "reward": "eat cake",
             "time_to_complete": 120,
             "user": self.user.pk}
        )

    def test_habit_update(self):
        """Тестирование изменения привычки"""
        # Создание тестовой привычки
        habit = Habit.objects.create(
            place="house",
            time="16:00:00",
            action="make homework",
            pleasant_habit=False,
            periodicity=1,
            reward="eat cake",
            is_public=True,
            time_to_complete=120,
            user=self.user

        )
        data = {'time': '17:00:00'}
        # Изменение привычки
        response = self.client.patch(reverse('habit:habit-update', args=[habit.pk]), data=data)

        # Проверка статуса
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        # Проверка вывода одной привычки
        self.assertEqual(
            response.json(),
            {'id': habit.pk,
             "date": None,
             "place": "house",
             "time": "17:00:00",
             "action": "make homework",
             "pleasant_habit": False,
             "related_habit": None,
             'is_public': True,
             "periodicity": 1,
             "reward": "eat cake",
             "time_to_complete": 120,
             "user": self.user.pk}
        )

    def test_habit_delete(self):
        """Тестирование удаления привычки"""
        # Создание тестовой привычки
        habit = Habit.objects.create(
            place="house",
            time="16:00:00",
            action="make homework",
            pleasant_habit=False,
            periodicity=1,
            reward="eat cake",
            is_public=True,
            time_to_complete=120,
            user=self.user
        )

        # Удаление тестовой привычки
        response = self.client.delete(reverse('habit:habit-delete', args=[habit.pk]))

        # Проверка статуса
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        # Проверка удаления привычки из БД
        self.assertFalse(Habit.objects.filter(pk=habit.pk).exists())
