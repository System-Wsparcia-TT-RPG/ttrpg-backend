from django.shortcuts import render, HttpResponse
from .models import Character

# Create your views here.

def home(request):
    return render(request, "home.html")

def characters(request):
    chars = Character.objects.all()
    return render(request, "characters.html", {"characters": chars})
