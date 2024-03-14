from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Класс для роли создателя"""
    message = "Доступно только создателю!"

    def has_object_permission(self, request, view, obj):
        """Метод для проверки принадлежности привычки создателю"""
        if request.user == obj.user:
            return True
        return False
