from json import loads
from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

import utils.spell_request_utils as spell_utils

from .models import (
    Player, DamageDice, Senses, Trait, Background, Action, Feature, Feat,
    Class, Details, Equipment, Weapon, Treasure, AbilityScores, Skills,
    SavingThrows, DeathSaves, CombatStats, Race, Spell, Components, Character
)
from .serializers import get_id_serializer, get_all_serializer


class CharacterView:
    class GetAll(APIView):
        def get(self, request: HttpRequest, depth: Optional[int] = None) -> JsonResponse:
            all_characters = Character.objects.all()
            serializer = get_all_serializer(Character, depth)

            return JsonResponse(serializer(all_characters, many=True).data, safe=False, status=200)

    class GetId(APIView):
        def get(self, request: HttpRequest, character_id: Optional[int] = None, depth: Optional[int] = None
                ) -> JsonResponse:
            try:
                character = Character.objects.get(id=character_id)
                serializer = get_all_serializer(Character, depth)

                return JsonResponse(serializer([character], many=True).data, safe=False, status=200)
            except ObjectDoesNotExist as error:
                return JsonResponse(
                    {
                        "error": "Character with specified id is not found!",
                        "details": {
                            "message": str(error),
                        },
                    },
                    safe=False,
                    status=404,
                )

    class ModifyId(APIView):
        def patch(self, request: HttpRequest, character_id: Optional[int]) -> JsonResponse:
            try:
                character = Character.objects.get(id=character_id)
            except ObjectDoesNotExist as error:
                return JsonResponse(
                    {
                        "error": "Character with specified id is not found!",
                        "details": {
                            "message": str(error),
                        },
                    },
                    safe=False,
                    status=404,
                )

            serializer_class = get_all_serializer(Character, None)
            serializer_id_class = get_id_serializer(Character, None)
            serializer = serializer_class(character, data=loads(request.body), partial=True)

            if serializer.is_valid():
                instance = serializer.save()
                return JsonResponse(serializer_id_class(instance).data, status=200)

            return JsonResponse(
                {
                    "error": "Invalid character data",
                    "details": serializer.errors
                },
                status=400,
            )

        def put(self, request: HttpRequest, character_id: Optional[int]) -> JsonResponse:
            serializer_class = get_all_serializer(Character, None)
            serializer_id_class = get_id_serializer(Character, None)

            try:
                character = Character.objects.get(id=character_id)
                serializer = serializer_class(character, data=loads(request.body))
                code: int = 200
            except ObjectDoesNotExist as _:
                serializer = serializer_class(data=loads(request.body))
                code: int = 201

            if serializer.is_valid():
                instance = serializer.save()
                return JsonResponse(serializer_id_class(instance).data, status=code)

            JsonResponse(
                {
                    "error": "Invalid character data",
                    "details": serializer.errors
                },
                status=400,
            )

        def delete(self, request: HttpRequest, character_id: Optional[int]) -> HttpResponse:
            try:
                count, _ = Character.objects.get(id=character_id).delete()

                return JsonResponse({"deleted_objects": count}, safe=False, status=200)
            except ObjectDoesNotExist as error:
                return JsonResponse(
                    {
                        "error": "Character with specified id is not found!",
                        "details": {
                            "message": str(error),
                        },
                    },
                    safe=False,
                    status=404,
                )

    class Create(APIView):
        def post(self, request: HttpRequest) -> JsonResponse:
            serializer_class = get_all_serializer(Character, None)
            serializer_id_class = get_id_serializer(Character, None)
            serializer = serializer_class(data=loads(request.body))

            if serializer.is_valid():
                instance = serializer.save()
                return JsonResponse(serializer_id_class(instance).data, status=201)

            return JsonResponse(
                {
                    "error": "Invalid character data",
                    "details": serializer.errors
                },
                status=400,
            )


class RaceView:
    class GetRaceEnum(APIView):
        def get(self, request: HttpRequest) -> JsonResponse:
            return JsonResponse(Race.Size.choices, status=200)


class SpellView:
    class Get(APIView):
        def get(self, request: HttpRequest) -> JsonResponse:
            all_spells = list(Spell.objects.values())

            return JsonResponse({"spells": all_spells})

    class Post(APIView):
        def post(self, request: HttpRequest) -> JsonResponse:
            json_data = loads(request)

            try:
                new_spell = spell_utils.create_spells_from_json(json_data)
                return JsonResponse({
                    "spell": {
                        "id": new_spell.id,
                        "data": {
                            **json_data
                        }
                    }
                }, status=201)
            except Exception as e:
                return JsonResponse({
                    "error": "An unexpected error occurred",
                    "details": str(e)
                }, status=500)


# Leave `http_method_names` as is, because we do not inherit from APIView here.
class Index(View):
    http_method_names = ['get']

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, 'index.html')
