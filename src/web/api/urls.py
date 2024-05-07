from django.urls import path
from . import views

urlpatterns = [
    path('api/characters/', views.CharacterView.Get.as_view()),
    path("api/character/<int:character_id>/", views.CharacterView.GetId.as_view()),
    path('api/character/create/', views.CharacterView.Post.as_view()),
    path('api/character/update/<int:character_id>/', views.CharacterView.Put.as_view()),
    path('api/character/delete/<int:character_id>/', views.CharacterView.Delete.as_view()),
    path('api/character/Race/Sizes/', views.CharacterView.Race.RaceSizeView.as_view()),
    path('', views.Index.as_view()),

]
