from django.shortcuts import render
from django.http import Http404

from .characters import characters


def index(request):
    context = {
        "title": "Catálogo de Legends",
        "characters": characters,
    }
    return render(request, "index.html", context)


def character_detail(request, slug):
    char = next((c for c in characters if c["slug"] == slug), None)
    if not char:
        raise Http404("Personaje no encontrado")
    context = {
        "title": char["name"],
        "character": char,
    }
    return render(request, "character_detail.html", context)
