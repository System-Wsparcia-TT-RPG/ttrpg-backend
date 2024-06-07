from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from utils.basic_crud_generator import (HasCreate, HasGetAll, HasGetId,
                                        HasModifyId, add_basic_crud)

from .models import (AbilityScores, Action, Background, Character, Class,
                     CombatStats, Components, DamageDice, DeathSaves, Details,
                     Equipment, Feat, Feature, Player, Race, SavingThrows,
                     Senses, Skills, Spell, Trait, Treasure, User, Weapon)
from .forms import SignUpForm


@add_basic_crud(Player, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class PlayerView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(DamageDice, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class DamageDiceView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    class GetSidesEnum(APIView):
        def get(self, request: HttpRequest) -> JsonResponse:
            return JsonResponse(DamageDice.Sides.choices, safe=False, status=200)


@add_basic_crud(Senses, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class SensesView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Trait, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class TraitView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Background, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class BackgroundView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Action, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class ActionView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Feature, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class FeatureView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Feat, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class FeatView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Class, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class ClassView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Details, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class DetailsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Equipment, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class EquipmentView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Weapon, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class WeaponView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Treasure, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class TreasureView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(AbilityScores, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class AbilityScoresView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Skills, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class SkillsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(SavingThrows, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class SavingThrowsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(DeathSaves, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class DeathSavesView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(CombatStats, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class CombatStatsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Race, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class RaceView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    class GetSizeEnum(APIView):
        def get(self, request: HttpRequest) -> JsonResponse:
            return JsonResponse(Race.Size.choices, safe=False, status=200)


@add_basic_crud(Components, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class ComponentsView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Spell, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class SpellView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(Character, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [IsAuthenticated],
})
class CharacterView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


@add_basic_crud(User, {
    'get_all': [IsAuthenticated],
    'get_id': [IsAuthenticated],
    'modify_id': [IsAuthenticated],
    'create': [AllowAny],
})
class UserView(HasGetAll, HasGetId, HasModifyId, HasCreate):
    pass


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
