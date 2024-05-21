from django.urls import path
from .views import (
    PlayerView, DamageDiceView, SensesView, TraitView, BackgroundView, ActionView, FeatureView, FeatView, ClassView, DetailsView, EquipmentView, WeaponView, TreasureView, AbilityScoresView, SkillsView, SavingThrowsView, DeathSavesView, CombatStatsView, RaceView, ComponentsView, SpellView, CharacterView
)

urlpatterns = [
    path('player/all/<int:depth>/', PlayerView.GetAll.as_view()),
    path('player/<int:identifier>/<int:depth>/', PlayerView.GetId.as_view()),
    path('player/<int:identifier>/', PlayerView.ModifyId.as_view()),
    path('player/create/', PlayerView.Create.as_view()),

    path('damage_dice/sides/possible/', RaceView.GetSidesEnum.as_view()),
    path('damage_dice/all/<int:depth>/', DamageDiceView.GetAll.as_view()),
    path('damage_dice/<int:identifier>/<int:depth>/', DamageDiceView.GetId.as_view()),
    path('damage_dice/<int:identifier>/', DamageDiceView.ModifyId.as_view()),
    path('damage_dice/create/', DamageDiceView.Create.as_view()),

    path('senses/all/<int:depth>/', SensesView.GetAll.as_view()),
    path('senses/<int:identifier>/<int:depth>/', SensesView.GetId.as_view()),
    path('senses/<int:identifier>/', SensesView.ModifyId.as_view()),
    path('senses/create/', SensesView.Create.as_view()),

    path('trait/all/<int:depth>/', TraitView.GetAll.as_view()),
    path('trait/<int:identifier>/<int:depth>/', TraitView.GetId.as_view()),
    path('trait/<int:identifier>/', TraitView.ModifyId.as_view()),
    path('trait/create/', TraitView.Create.as_view()),

    path('background/all/<int:depth>/', BackgroundView.GetAll.as_view()),
    path('background/<int:identifier>/<int:depth>/', BackgroundView.GetId.as_view()),
    path('background/<int:identifier>/', BackgroundView.ModifyId.as_view()),
    path('background/create/', BackgroundView.Create.as_view()),

    path('action/all/<int:depth>/', ActionView.GetAll.as_view()),
    path('action/<int:identifier>/<int:depth>/', ActionView.GetId.as_view()),
    path('action/<int:identifier>/', ActionView.ModifyId.as_view()),
    path('action/create/', ActionView.Create.as_view()),

    path('feature/all/<int:depth>/', FeatureView.GetAll.as_view()),
    path('feature/<int:identifier>/<int:depth>/', FeatureView.GetId.as_view()),
    path('feature/<int:identifier>/', FeatureView.ModifyId.as_view()),
    path('feature/create/', FeatureView.Create.as_view()),

    path('feat/all/<int:depth>/', FeatView.GetAll.as_view()),
    path('feat/<int:identifier>/<int:depth>/', FeatView.GetId.as_view()),
    path('feat/<int:identifier>/', FeatView.ModifyId.as_view()),
    path('feat/create/', FeatView.Create.as_view()),

    path('class/all/<int:depth>/', ClassView.GetAll.as_view()),
    path('class/<int:identifier>/<int:depth>/', ClassView.GetId.as_view()),
    path('class/<int:identifier>/', ClassView.ModifyId.as_view()),
    path('class/create/', ClassView.Create.as_view()),

    path('details/all/<int:depth>/', DetailsView.GetAll.as_view()),
    path('details/<int:identifier>/<int:depth>/', DetailsView.GetId.as_view()),
    path('details/<int:identifier>/', DetailsView.ModifyId.as_view()),
    path('details/create/', DetailsView.Create.as_view()),

    path('equipment/all/<int:depth>/', EquipmentView.GetAll.as_view()),
    path('equipment/<int:identifier>/<int:depth>/', EquipmentView.GetId.as_view()),
    path('equipment/<int:identifier>/', EquipmentView.ModifyId.as_view()),
    path('equipment/create/', EquipmentView.Create.as_view()),

    path('weapon/all/<int:depth>/', WeaponView.GetAll.as_view()),
    path('weapon/<int:identifier>/<int:depth>/', WeaponView.GetId.as_view()),
    path('weapon/<int:identifier>/', WeaponView.ModifyId.as_view()),
    path('weapon/create/', WeaponView.Create.as_view()),

    path('treasure/all/<int:depth>/', TreasureView.GetAll.as_view()),
    path('treasure/<int:identifier>/<int:depth>/', TreasureView.GetId.as_view()),
    path('treasure/<int:identifier>/', TreasureView.ModifyId.as_view()),
    path('treasure/create/', TreasureView.Create.as_view()),

    path('ability_scores/all/<int:depth>/', AbilityScoresView.GetAll.as_view()),
    path('ability_scores/<int:identifier>/<int:depth>/', AbilityScoresView.GetId.as_view()),
    path('ability_scores/<int:identifier>/', AbilityScoresView.ModifyId.as_view()),
    path('ability_scores/create/', AbilityScoresView.Create.as_view()),

    path('skills/all/<int:depth>/', SkillsView.GetAll.as_view()),
    path('skills/<int:identifier>/<int:depth>/', SkillsView.GetId.as_view()),
    path('skills/<int:identifier>/', SkillsView.ModifyId.as_view()),
    path('skills/create/', SkillsView.Create.as_view()),

    path('saving_throws/all/<int:depth>/', SavingThrowsView.GetAll.as_view()),
    path('saving_throws/<int:identifier>/<int:depth>/', SavingThrowsView.GetId.as_view()),
    path('saving_throws/<int:identifier>/', SavingThrowsView.ModifyId.as_view()),
    path('saving_throws/create/', SavingThrowsView.Create.as_view()),

    path('death_saves/all/<int:depth>/', DeathSavesView.GetAll.as_view()),
    path('death_saves/<int:identifier>/<int:depth>/', DeathSavesView.GetId.as_view()),
    path('death_saves/<int:identifier>/', DeathSavesView.ModifyId.as_view()),
    path('death_saves/create/', DeathSavesView.Create.as_view()),

    path('combat_stats/all/<int:depth>/', CombatStatsView.GetAll.as_view()),
    path('combat_stats/<int:identifier>/<int:depth>/', CombatStatsView.GetId.as_view()),
    path('combat_stats/<int:identifier>/', CombatStatsView.ModifyId.as_view()),
    path('combat_stats/create/', CombatStatsView.Create.as_view()),

    path('race/size/possible/', RaceView.GetSizeEnum.as_view()),
    path('race/all/<int:depth>/', RaceView.GetAll.as_view()),
    path('race/<int:identifier>/<int:depth>/', RaceView.GetId.as_view()),
    path('race/<int:identifier>/', RaceView.ModifyId.as_view()),
    path('race/create/', RaceView.Create.as_view()),

    path('components/all/<int:depth>/', ComponentsView.GetAll.as_view()),
    path('components/<int:identifier>/<int:depth>/', ComponentsView.GetId.as_view()),
    path('components/<int:identifier>/', ComponentsView.ModifyId.as_view()),
    path('components/create/', ComponentsView.Create.as_view()),

    path('spell/all/<int:depth>/', SpellView.GetAll.as_view()),
    path('spell/<int:identifier>/<int:depth>/', SpellView.GetId.as_view()),
    path('spell/<int:identifier>/', SpellView.ModifyId.as_view()),
    path('spell/create/', SpellView.Create.as_view()),

    path('character/all/<int:depth>/', CharacterView.GetAll.as_view()),
    path('character/<int:identifier>/<int:depth>/', CharacterView.GetId.as_view()),
    path('character/<int:identifier>/', CharacterView.ModifyId.as_view()),
    path('character/create/', CharacterView.Create.as_view()),
]
