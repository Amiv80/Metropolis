from django.urls import path
from core.views import game_view

urlpatterns = [
    path('', game_view, name='game'),
]