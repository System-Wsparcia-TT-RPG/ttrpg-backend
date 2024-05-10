from json import load, loads

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View

from utils.character_validation import CharacterSerializer
from utils.http_options_decorator import add_http_options

from .models import Character, Race


class CharacterView:
    @add_http_options
    class Get(View):
        http_method_names = ["get"]

        @staticmethod
        def get(request) -> JsonResponse:
            all_characters = list(Character.objects.values())

            return JsonResponse({"characters": all_characters})

    @add_http_options
    class GetId(View):
        http_method_names = ["get"]

        @staticmethod
        def get(request, character_id: int) -> JsonResponse:
            try:
                character = Character.objects.values().get(id=character_id)

                return JsonResponse({"character": character}, status=200)
            except ObjectDoesNotExist as error:
                return JsonResponse({
                    "error": "Character with specified id is not found!",
                    "details": str(error),
                    "error_data": {
                        "id_not_found": character_id,
                    },
                }, status=404)

    @add_http_options
    class Post(View):
        http_method_names = ["post"]

        @staticmethod
        def post(request) -> JsonResponse:
            json_data = loads(request.body)
            
            # Validation
            data_ser = CharacterSerializer(data=json_data)
            if data_ser.is_valid():
                return JsonResponse({"character": {"id": 2, "data": {**json_data}}}, status=201)
            else:
                return JsonResponse({"error": "Provided character data is invalid!"}, status=400)

    @add_http_options
    class Put(View):
        http_method_names = ["put"]

        @staticmethod
        def put(request, character_id: int) -> JsonResponse:
            if character_id != 1:
                return JsonResponse({"error": "Character not found"}, status=404)

            with open("./src/web/api/static_json/1.json", "r", encoding="utf-8") as file:
                return JsonResponse({"character": load(file)})

    @add_http_options
    class Delete(View):
        http_method_names = ["delete"]

        @staticmethod
        def delete(request, character_id: int) -> HttpResponse:
            if character_id != 1:
                return JsonResponse({"error": "Character not found"}, status=404)

            return HttpResponse(status=204)

class RaceView:
    @add_http_options
    class GetRaceEnum(View):
        http_method_names = ['get']

        @staticmethod
        def get(request) -> JsonResponse:
            return JsonResponse({a: a.value for a in Race.Size}, status=200)


@add_http_options
class Index(View):
    http_method_names = ['get']

    @staticmethod
    def get(request) -> HttpResponse:
        return render(request, 'index.html')
