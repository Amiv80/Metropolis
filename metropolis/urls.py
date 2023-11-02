from django.urls import path
from core.views import game_view, tutorial_view, overview_view

urlpatterns = [
    path("", game_view, name="game"),
    path("tutorial/", tutorial_view, name="tutorial"),
    path("overview/", overview_view, name="overview"),
]
