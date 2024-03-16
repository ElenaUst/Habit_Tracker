from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User
from users.serializers import UserRegisterSerializer, UserSerializer


class UserRegister(generics.CreateAPIView):
    """Класс для регистрации пользователя"""
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        """Метод для хэширования пароля пользователя в БД"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieve(generics.RetrieveAPIView):
    """Класс для просмотра пользователя"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserUpdate(generics.UpdateAPIView):
    """Класс для обновления пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserList(generics.ListAPIView):
    """Класс для просмотра списка пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

