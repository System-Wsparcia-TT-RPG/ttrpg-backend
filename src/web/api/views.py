from json import loads
from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View

import utils.character_request_utils as character_utils
import utils.spell_request_utils as spell_utils
from utils.http_options_decorator import add_http_options

from .models import (
    Player, DamageDice, Senses, Trait, Background, Action, Feature, Feat,
    Class, Details, Equipment, Weapon, Treasure, AbilityScores, Skills,
    SavingThrows, DeathSaves, CombatStats, Race, Spell, Components, Character
)
from .serializers import get_id_serializer, get_all_serializer


class CharacterView:
    @add_http_options
    class GetAll(View):
        http_method_names = ["get"]

        @staticmethod
        def get(request: HttpRequest, depth: Optional[int] = None) -> JsonResponse:
            all_characters = Character.objects.all()
            serializer = get_all_serializer(
                Character,
                depth,
            )

            return JsonResponse(
                serializer(all_characters, many=True).data,
                safe=False,
                status=200,
            )

    @add_http_options
    class GetId(View):
        http_method_names = ["get"]

        @staticmethod
        def get(request: HttpRequest, character_id: Optional[int] = None, depth: Optional[int] = None) -> JsonResponse:
            try:
                character = Character.objects.get(id=character_id)
                serializer = get_all_serializer(
                    Character,
                    depth,
                )

                return JsonResponse(
                    serializer([character], many=True).data,
                    safe=False,
                    status=200,
                )
            except ObjectDoesNotExist as error:
                return JsonResponse(
                    {
                        "error": "Character with specified id is not found!",
                        "details": str(error),
                        "error_data": {
                            "character_id": character_id,
                            "depth": depth,
                        },
                    },
                    status=404,
                )

    @add_http_options
    class ModifyId(View):
        http_method_names = ["put", "delete"]

        def put(self, request: HttpRequest, character_id: Optional[int]) -> JsonResponse:
            if character_id < 0:
                return JsonResponse({
                    "error": "Invalid character ID"
                }, status=400)

            json_data = loads(request.body)

            class CharacterSerializer:
                pass

            # Validation
            data_ser = CharacterSerializer(data=json_data)
            if data_ser.is_valid():
                Character.objects.filter(id=character_id).update(**data_ser)
                return JsonResponse({
                    "character": {
                        "id": character_id,
                        "data": {
                            **json_data
                        }
                    }
                }, status=201)
            else:
                return JsonResponse({
                    "error": "Provided character data is invalid"
                }, status=400)

        def delete(self, request: HttpRequest, character_id: Optional[int]) -> HttpResponse:

            try:
                Character.objects.filter(id=character_id).delete()
            except ObjectDoesNotExist as error:
                return JsonResponse({
                    "error": "Character not found",
                    "details": str(error),
                    "error_data": {
                        "id_not_found": character_id,
                    }
                }, status=404)

            return HttpResponse(status=204)

    @add_http_options
    class Post(View):
        http_method_names = ["post"]

        @staticmethod
        def post(request: HttpRequest) -> JsonResponse:
            json_data = loads(request.body)

            class CharacterSerializer:
                pass

            # Validation and db entry creation
            data_ser = CharacterSerializer(data=json_data)
            if data_ser.is_valid():
                try:
                    new_char = character_utils.create_character_from_json(json_data)
                    return JsonResponse({
                        "character": {
                            "id": new_char.id,
                            "data": {
                                **json_data
                            }
                        }
                    }, status=201)
                except Exception as e:
                    print("An unexpected Exception occured: ", str(e))
            else:
                return JsonResponse({"error": "Provided character data is invalid!"}, status=400)


class RaceView:
    @add_http_options
    class GetRaceEnum(View):
        http_method_names = ['get']

        @staticmethod
        def get(request: HttpRequest) -> JsonResponse:
            return JsonResponse([a.value for a in Race.Size], status=200)


class SpellView:
    @add_http_options
    class Get(View):
        http_method_names = ['get']

        @staticmethod
        def get(request: HttpRequest) -> JsonResponse:
            all_spells = list(Spell.objects.values())

            return JsonResponse({"spells": all_spells})

    @add_http_options
    class Post(View):
        http_method_names = ['post']

        @staticmethod
        def post(request: HttpRequest) -> JsonResponse:
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


@add_http_options
class Index(View):
    http_method_names = ['get']

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, 'index.html')
