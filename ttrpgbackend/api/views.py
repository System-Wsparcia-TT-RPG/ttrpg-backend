from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Character

# Create your views here.

def home(request):
    return render(request, "home.html")

def characters(request):
    chars = Character.objects.all()
    return render(request, "characters.html", {"characters": chars})

def api_characters(request):
    return JsonResponse({"characters": list(Character.objects.values())})
