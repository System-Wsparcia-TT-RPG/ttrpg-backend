from json import load, loads

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View


from .models import Character
from .models import Race

from utils.character_validation import CharacterSerializer

class CharacterView:
    class Get(View):
        http_method_names = ["get"]

        @staticmethod
        def get(request) -> JsonResponse:
            with open("./src/web/api/static_json/1.json", "r", encoding="utf-8") as file:
                return JsonResponse({"characters": [{"id": 1, "data": load(file)},]})

    class GetId(View):
        http_method_names = ["get"]

        @staticmethod
        def get(request, character_id: int) -> JsonResponse:
            if character_id != 1:
                return JsonResponse({"error": "Character not found"}, status=404)

            with open("./src/web/api/static_json/1.json", "r", encoding="utf-8") as file:
                return JsonResponse({"character": load(file)})

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

    class Put(View):
        http_method_names = ["put"]

        @staticmethod
        def put(request, character_id: int) -> JsonResponse:
            if character_id != 1:
                return JsonResponse({"error": "Character not found"}, status=404)

            with open("./src/web/api/static_json/1.json", "r", encoding="utf-8") as file:
                return JsonResponse({"character": load(file)})

    class Delete(View):
        http_method_names = ["delete"]

        @staticmethod
        def delete(request, character_id: int) -> HttpResponse:
            if character_id != 1:
                return JsonResponse({"error": "Character not found"}, status=404)

            return HttpResponse(status=204)

    class RaceView:
        class GetRaceSizes(View):
            http_method_names = ['get']

            @staticmethod
            def get(request) -> JsonResponse:
                return JsonResponse({a : a.value for a in (Race.Size)}, status = 201)