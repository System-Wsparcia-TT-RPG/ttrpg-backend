from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.basic_crud_generator import (HasCreate, HasGetAll, HasGetId,
                                        HasModifyId, add_basic_crud)

from .models import (AbilityScores, Action, Background, Character, Class,
                     CombatStats, Components, DamageDice, DeathSaves, Details,
                     Equipment, Feat, Feature, Player, Race, SavingThrows,
                     Senses, Skills, Spell, Trait, Treasure, User, Weapon)


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

@add_basic_crud(User)
class UserView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass

# Leave `http_method_names` as is, because we do not inherit from APIView here.
class Index(View):
    http_method_names = ['get']

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, 'index.html')

@api_view(['POST'])
def receive_data(request):
    data = str(request.data) #ZNACZNIK
    '''
    Na razie zakładam, że podane dane to będzie informacja w słowniku,
    czy to rejestracja, czy login i opisane dane, np:
    {"operation": "R", "login": "nazwa", "password": "hasło", "email": "email"}
    {"operation": "L", "login": "nazwa", "password": "hasło"}
    '''
    if data[0] == 'R':
        new_user = User(login=data["login"], password=data["password"], email=data["email"])
        new_user.save()
        return Response({'message': 'Użytkownik zarejestrowany'}, status=status.HTTP_200_OK)
    elif data[0] == 'L':
        user = User.objects.filter(login=data["login"])
        if len(user) == 1:
            if user.password == data["password"]:
                return Response({'message': 'Użytkownik istnieje'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Użytkownik nie istnieje'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Nieprawidłowe dane'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Nieznana operacja'}, status=status.HTTP_200_OK)