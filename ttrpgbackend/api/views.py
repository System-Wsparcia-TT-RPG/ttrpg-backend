from json import load

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Character


# Create your views here.

def home(request):
    return render(request, "home.html")


def characters(request):
    chars = Character.objects.all()
    return render(request, "characters.html", {"characters": chars})


def api_character(request, id: int=1):
    with open("./api/static_json/1.json", "r", encoding="utf-8") as file:
        return JsonResponse({"character": load(file)})
