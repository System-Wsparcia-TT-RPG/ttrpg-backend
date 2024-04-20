from json import load

from django.http import JsonResponse
from django.shortcuts import render

from .models import Character
from utils.example import example


# Create your views here.

def home(request):
    return render(request, "home.html")


def characters(request):
    chars = Character.objects.all()
    example()
    return render(request, "characters.html", {"characters": chars})


def api_character(request):
    with open("./src/web/api/static_json/1.json", "r", encoding="utf-8") as file:
        return JsonResponse({"character": load(file)})
    # to change to dynamic with Character model, use dump function to serialize the model to json, then return JsonResponse
