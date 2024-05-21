from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

from utils.basic_crud_generator import add_basic_crud, HasGetAll, HasGetId, HasModifyId, HasCreate
from .models import (
    Player, DamageDice, Senses, Trait, Background, Action, Feature, Feat, Class, Details, Equipment, Weapon, Treasure,
    AbilityScores, Skills, SavingThrows, DeathSaves, CombatStats, Race, Components, Spell, Character
)


@add_basic_crud(Player)
class PlayerView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(DamageDice)
class DamageDiceView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    class GetSidesEnum(APIView):
        def get(self, request: HttpRequest) -> JsonResponse:
            return JsonResponse(DamageDice.Sides.choices, safe=False, status=200)


@add_basic_crud(Senses)
class SensesView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Trait)
class TraitView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Background)
class BackgroundView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Action)
class ActionView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Feature)
class FeatureView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Feat)
class FeatView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Class)
class ClassView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Details)
class DetailsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Equipment)
class EquipmentView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Weapon)
class WeaponView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Treasure)
class TreasureView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(AbilityScores)
class AbilityScoresView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Skills)
class SkillsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(SavingThrows)
class SavingThrowsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(DeathSaves)
class DeathSavesView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(CombatStats)
class CombatStatsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Race)
class RaceView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    class GetSizeEnum(APIView):
        def get(self, request: HttpRequest) -> JsonResponse:
            return JsonResponse(Race.Size.choices, safe=False, status=200)


@add_basic_crud(Components)
class ComponentsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Spell)
class SpellView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Character)
class CharacterView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


# Leave `http_method_names` as is, because we do not inherit from APIView here.
class Index(View):
    http_method_names = ['get']

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, 'index.html')
