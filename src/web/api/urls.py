from django.urls import path
from . import views

urlpatterns = [
    path('character/all/<int:depth>/', views.CharacterView.GetAll.as_view()),
    path("character/<int:character_id>/<int:depth>/", views.CharacterView.GetId.as_view()),
    path('character/create/', views.CharacterView.Post.as_view()),

    path('race/possible/', views.RaceView.GetRaceEnum.as_view()),
    path('race/all/', views.RaceView.GetRaceEnum.as_view()),

    path('spell/all/', views.SpellView.Get.as_view()),
    path('spell/create/', views.SpellView.Post.as_view()),
]
