from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = HabitConfig.name


urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit-list'),
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('detail/<int:pk>', HabitRetrieveAPIView.as_view(), name='habit-detail'),
    path('update/<int:pk>', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('delete/<int:pk>', HabitDestroyAPIView.as_view(), name='habit-delete'),
]

