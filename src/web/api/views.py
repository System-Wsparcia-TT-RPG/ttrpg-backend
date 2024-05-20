from json import loads

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View

import utils.character_request_utils as character_utils
import utils.spell_request_utils as spell_utils
from utils.character_validation import CharacterSerializer
from utils.http_options_decorator import add_http_options
from .models import *


class CharacterView:
    @add_http_options
    class Get(View):
        http_method_names = ["get"]

        @staticmethod
        def get(request) -> JsonResponse:
            all_characters = list(Character.objects.values())

            return JsonResponse({
                "characters": all_characters
            })

    @add_http_options
    class GetId(View):
        http_method_names = ["get", "put", "delete"]

        @staticmethod
        def get(request, character_id: int) -> JsonResponse:
            try:
                character = character_utils.get_character(character_id)

                return JsonResponse({
                    "character": character
                }, status=200)
            except ObjectDoesNotExist as error:
                return JsonResponse({
                    "error": "Character with specified id is not found!",
                    "details": str(error),
                    "error_data": {
                        "id_not_found": character_id,
                    },
                }, status=404)

        @staticmethod
        def put(request, character_id: int) -> JsonResponse:
            if character_id < 0:
                return JsonResponse({
                    "error": "Invalid character ID"
                }, status=400)

            json_data = loads(request.body)

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

        @staticmethod
        def delete(request, character_id: int) -> HttpResponse:

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
        def post(request) -> JsonResponse:
            json_data = loads(request.body)

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
        def get(request) -> JsonResponse:
            return JsonResponse([a.value for a in Race.Size], status=200)


class SpellView:
    @add_http_options
    class Get(View):
        http_method_names = ['get']

        @staticmethod
        def get(request) -> JsonResponse:
            all_spells = list(Spell.objects.values())

            return JsonResponse({"spells": all_spells})

    @add_http_options
    class Post(View):
        http_method_names = ['post']

        @staticmethod
        def post(request) -> JsonResponse:
            json_data = loads(request.body)

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
    def get(request) -> HttpResponse:
        return render(request, 'index.html')
