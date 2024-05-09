from django.urls import path
from . import views

urlpatterns = [
    path('character/all/', views.CharacterView.Get.as_view()),
    path("character/<int:character_id>/", views.CharacterView.GetId.as_view()),
    path('character/create/', views.CharacterView.Post.as_view()),
    path('character/update/<int:character_id>/', views.CharacterView.Put.as_view()),
    path('character/delete/<int:character_id>/', views.CharacterView.Delete.as_view()),
    path('race/all/', views.RaceView.GetRaceEnum.as_view()),
    path('', views.Index.as_view()),

]
