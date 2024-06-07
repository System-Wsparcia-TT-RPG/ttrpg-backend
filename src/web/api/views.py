from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView
from utils.basic_crud_generator import (HasCreate, HasGetAll, HasGetId,
                                        HasModifyId, add_get_all, add_get_id, add_modify_id, add_create)
from json import loads
from web.api.serializers import UserSerializer, get_all_serializer, get_id_serializer
from django.contrib.auth.hashers import make_password


from .models import (AbilityScores, Action, Background, Character, Class,
                     CombatStats, Components, DamageDice, DeathSaves, Details,
                     Equipment, Feat, Feature, Player, Race, SavingThrows,
                     Senses, Skills, Spell, Trait, Treasure, User, Weapon)
from .forms import SignUpForm


# @add_basic_crud(Player, {
#     'get_all': [IsAuthenticated],
#     'get_id': [IsAuthenticated],
#     'modify_id': [IsAuthenticated],
#     'create': [IsAuthenticated],
# })
# class PlayerView(HasGetAll, HasGetId, HasModifyId, HasCreate):
#     pass

@add_get_all(Player, [IsAuthenticated])
@add_get_id(Player, [IsAuthenticated])
@add_modify_id(Player, [IsAuthenticated])
@add_create(Player, [IsAuthenticated])
class PlayerView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(DamageDice, [IsAuthenticated])
@add_get_id(DamageDice, [IsAuthenticated])
@add_modify_id(DamageDice, [IsAuthenticated])
@add_create(DamageDice, [IsAuthenticated])
class DamageDiceView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    class GetSidesEnum(APIView):
        def get(self, request: HttpRequest) -> JsonResponse:
            return JsonResponse(DamageDice.Sides.choices, safe=False, status=200)


@add_get_all(Senses, [IsAuthenticated])
@add_get_id(Senses, [IsAuthenticated])
@add_modify_id(Senses, [IsAuthenticated])
@add_create(Senses, [IsAuthenticated])
class SensesView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(Trait, [IsAuthenticated])
@add_get_id(Trait, [IsAuthenticated])
@add_modify_id(Trait, [IsAuthenticated])
@add_create(Trait, [IsAuthenticated])
class TraitView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(Background, [IsAuthenticated])
@add_get_id(Background, [IsAuthenticated])
@add_modify_id(Background, [IsAuthenticated])
@add_create(Background, [IsAuthenticated])
class BackgroundView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(Action, [IsAuthenticated])
@add_get_id(Action, [IsAuthenticated])
@add_modify_id(Action, [IsAuthenticated])
@add_create(Action, [IsAuthenticated])
class ActionView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(Feature, [IsAuthenticated])
@add_get_id(Feature, [IsAuthenticated])
@add_modify_id(Feature, [IsAuthenticated])
@add_create(Feature, [IsAuthenticated])
class FeatureView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(Feat, [IsAuthenticated])
@add_get_id(Feat, [IsAuthenticated])
@add_modify_id(Feat, [IsAuthenticated])
@add_create(Feat, [IsAuthenticated])
class FeatView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(Class, [IsAuthenticated])
@add_get_id(Class, [IsAuthenticated])
@add_modify_id(Class, [IsAuthenticated])
@add_create(Class, [IsAuthenticated])
class ClassView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(Details, [IsAuthenticated])
@add_get_id(Details, [IsAuthenticated])
@add_modify_id(Details, [IsAuthenticated])
@add_create(Details, [IsAuthenticated])
class DetailsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(Equipment, [IsAuthenticated])
@add_get_id(Equipment, [IsAuthenticated])
@add_modify_id(Equipment, [IsAuthenticated])
@add_create(Equipment, [IsAuthenticated])
class EquipmentView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(Weapon, [IsAuthenticated])
@add_get_id(Weapon, [IsAuthenticated])
@add_modify_id(Weapon, [IsAuthenticated])
@add_create(Weapon, [IsAuthenticated])
class WeaponView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(Treasure, [IsAuthenticated])
@add_get_id(Treasure, [IsAuthenticated])
@add_modify_id(Treasure, [IsAuthenticated])
@add_create(Treasure, [IsAuthenticated])
class TreasureView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(AbilityScores, [IsAuthenticated])
@add_get_id(AbilityScores, [IsAuthenticated])
@add_modify_id(AbilityScores, [IsAuthenticated])
@add_create(AbilityScores, [IsAuthenticated])
class AbilityScoresView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(Skills, [IsAuthenticated])
@add_get_id(Skills, [IsAuthenticated])
@add_modify_id(Skills, [IsAuthenticated])
@add_create(Skills, [IsAuthenticated])
class SkillsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(SavingThrows, [IsAuthenticated])
@add_get_id(SavingThrows, [IsAuthenticated])
@add_modify_id(SavingThrows, [IsAuthenticated])
@add_create(SavingThrows, [IsAuthenticated])
class SavingThrowsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(DeathSaves, [IsAuthenticated])
@add_get_id(DeathSaves, [IsAuthenticated])
@add_modify_id(DeathSaves, [IsAuthenticated])
@add_create(DeathSaves, [IsAuthenticated])
class DeathSavesView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(CombatStats, [IsAuthenticated])
@add_get_id(CombatStats, [IsAuthenticated])
@add_modify_id(CombatStats, [IsAuthenticated])
@add_create(CombatStats, [IsAuthenticated])
class CombatStatsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(CombatStats, [IsAuthenticated])
@add_get_id(CombatStats, [IsAuthenticated])
@add_modify_id(CombatStats, [IsAuthenticated])
@add_create(CombatStats, [IsAuthenticated])
class RaceView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    class GetSizeEnum(APIView):
        def get(self, request: HttpRequest) -> JsonResponse:
            return JsonResponse(Race.Size.choices, safe=False, status=200)


@add_get_all(Components, [IsAuthenticated])
@add_get_id(Components, [IsAuthenticated])
@add_modify_id(Components, [IsAuthenticated])
@add_create(Components, [IsAuthenticated])
class ComponentsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(Spell, [IsAuthenticated])
@add_get_id(Spell, [IsAuthenticated])
@add_modify_id(Spell, [IsAuthenticated])
@add_create(Spell, [IsAuthenticated])
class SpellView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(Character, [IsAuthenticated])
@add_get_id(Character, [IsAuthenticated])
@add_modify_id(Character, [IsAuthenticated])
@add_create(Character, [IsAuthenticated])
class CharacterView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_get_all(User, [IsAuthenticated])
@add_get_id(User, [IsAuthenticated])
@add_modify_id(User, [IsAuthenticated])
class UserView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    class Create(APIView):
        # serializer_class = get_all_serializer(User, None)
        serializer_class = UserSerializer
        
        serializer_id_class = get_id_serializer(User, None)
        permission_classes = [AllowAny]

        def post(self, request: HttpRequest) -> JsonResponse:
            request_data = loads(request.body)
            request_data['password'] = make_password(request_data['password'])
            serializer = self.serializer_class(data=request_data)

            if serializer.is_valid():
                instance = serializer.save()
                return JsonResponse(self.serializer_id_class(instance).data, status=201)

            return JsonResponse(
                {
                    "error": f"Invalid \'{User.__class__.__name__}\' data!",
                    "details": serializer.errors
                },
                status=400,
            )


# Leave `http_method_names` as is, because we do not inherit from APIView here.
class Index(View):
    http_method_names = ['get']

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, 'index.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Utworzono nowe konto użutkownika')
            return redirect('/api/login/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/api/home/')
        else:
            return render(request, 'login.html', {'error': 'Nieprawidłowa nazwa użytkowanika lub hasło'})
    else:
        return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/api/login/')


def home_view(request):
    """
    Do testów autentykacji
    """
    return render(request, 'home.html')
