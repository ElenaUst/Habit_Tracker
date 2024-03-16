from rest_framework import status


from users.models import User
from rest_framework.test import APITestCase, APIClient


class UserTestCase(APITestCase):
    """Тестирование CRUD для пользователя"""

    def setUp(self) -> None:
        self.client = APIClient()
        # Создание тестового пользователя
        self.user = User.objects.create(
            email="test@test.com",
            password="test",
            telegram='123456789'
        )
        # Аутентификация тестового пользователя
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """Тестирование создания пользователя"""

        data = {
            "email": 'test_create@test.com',
            "password": '12345',
            "telegram": '123456789'
        }

        response = self.client.post('/users/create/', data=data)

        # Проверка наличия записи в БД
        self.assertTrue(
            User.objects.all().exists()
        )

        # Проверка статуса
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        # Проверка создания пользователя
        self.assertEqual(
            response.json()
            ['email'], 'test_create@test.com')
