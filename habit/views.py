from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.paginators import CustomPagination
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Класс для создания привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Метод для автоматической привязки привычки к создателю"""
        serializer.save(user=self.request.user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Класс для просмотра одной привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Класс для изменения привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitListAPIView(generics.ListAPIView):
    """Класс для просмотра списка публичных привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        """Отображение только публичных привычек"""
        return Habit.objects.filter(is_public=True)


class HabitOwnerListAPIView(generics.ListAPIView):
    """Класс для просмотра списка привычек пользователя"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        """Отображение привычек пользователя"""
        return Habit.objects.filter(user=self.request.user)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Класс для удаления привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


