from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("characters/", views.characters, name="characters"),
    path("api/characters/", views.api_characters, name="api_characters"),
]
