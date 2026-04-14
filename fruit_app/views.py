from django.http import HttpRequest, JsonResponse
from django.shortcuts import render


def send_fruits(request: HttpRequest):
    fruits: list[dict[str, str | int]] = [
        {"name": "Apfel", "gewicht": 150, "farbe": "Rot"},
        {"name": "Banane", "gewicht": 120, "farbe": "Gelb"},
        {"name": "Orange", "gewicht": 200, "farbe": "Orange"},
        {"name": "Kirsche", "gewicht": 10, "farbe": "Rot"},
        {"name": "Ananas", "gewicht": 1000, "farbe": "Gelb"},
    ]
    # Hier passiert der Fehler ohne safe=False
    return JsonResponse(fruits, safe=False)


def send_fruits_template(request: HttpRequest | None):
    fruits: list[dict[str, str | int]] = [
        {"name": "Apfel", "gewicht": 150, "farbe": "Rot"},
        {"name": "Banane", "gewicht": 120, "farbe": "Gelb"},
        {"name": "Orange", "gewicht": 200, "farbe": "Orange"},
        {"name": "Kirsche", "gewicht": 10, "farbe": "Rot"},
        {"name": "Ananas", "gewicht": 1000, "farbe": "Gelb"},
    ]
    context: dict[str, list[dict[str, str | int]]] = {"fruits": fruits}
    # Hier passiert der Fehler ohne safe=False
    return render(request, "fruit_app/fruitlist.html", context)
