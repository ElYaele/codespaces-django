from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .characters import characters
from .serializers import CharacterSerializer


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


@api_view(['GET'])
def api_characters_list(request):
    """
    API endpoint que devuelve la lista de todos los personajes
    """
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_character_detail(request, slug):
    """
    API endpoint que devuelve los detalles de un personaje específico
    """
    char = next((c for c in characters if c["slug"] == slug), None)
    if not char:
        return Response({"error": "Personaje no encontrado"}, status=404)
    
    serializer = CharacterSerializer(char)
    return Response(serializer.data)

