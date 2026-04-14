from django.http import HttpRequest, JsonResponse
from django.shortcuts import render


def send_fruits(request: HttpRequest):
    # fruits: list[dict[str, str | int]] = [
    #     {"name": "Apfel", "gewicht": 150, "farbe": "Rot"},
    #     {"name": "Banane", "gewicht": 120, "farbe": "Gelb"},
    #     {"name": "Orange", "gewicht": 200, "farbe": "Orange"},
    #     {"name": "Kirsche", "gewicht": 10, "farbe": "Rot"},
    #     {"name": "Ananas", "gewicht": 1000, "farbe": "Gelb"},
    # ]
    # Hier passiert der Fehler ohne safe=False
    return JsonResponse(fruits, safe=False)


def send_fruits_template(request: HttpRequest | None):
    # fruits: list[dict[str, str | int]] = [
    #     {"name": "Apfel", "gewicht": 150, "farbe": "Rot"},
    #     {"name": "Banane", "gewicht": 120, "farbe": "Gelb"},
    #     {"name": "Orange", "gewicht": 200, "farbe": "Orange"},
    #     {"name": "Kirsche", "gewicht": 10, "farbe": "Rot"},
    #     {"name": "Ananas", "gewicht": 1000, "farbe": "Gelb"},
    # ]
    context: dict[str, list[dict[str, str | int]]] = {"fruits": fruits}
    # Hier passiert der Fehler ohne safe=False
    return render(request, "fruit_app/fruitlist.html", context)


def fruit_info(request: HttpRequest | None):
    # fruits: list[dict[str, str | int]] = [
    #     {"name": "Apfel", "gewicht": 150, "farbe": "Rot"},
    #     {"name": "Banane", "gewicht": 120, "farbe": "Gelb"},
    #     {"name": "Orange", "gewicht": 200, "farbe": "Orange"},
    #     {"name": "Kirsche", "gewicht": 10, "farbe": "Rot"},
    #     {"name": "Ananas", "gewicht": 1000, "farbe": "Gelb"},
    # ]
    return render(request, "fruit_app/info.html", fruits[0])


fruits: list[dict[str, str | int]] = [
    {
        "name": "Apfel",
        "gewicht": 150,
        "farbe": "Rot",
        "img": "../../static/fruit_app/img/apfel.webp",
    },
    {
        "name": "Banane",
        "gewicht": 120,
        "farbe": "Gelb",
        "img": "../../static/fruit_app/img/banane.jpg",
    },
    {
        "name": "Orange",
        "gewicht": 200,
        "farbe": "Orange",
        "img": "../../static/fruit_app/img/orange.jpg",
    },
    {
        "name": "Kirsche",
        "gewicht": 10,
        "farbe": "Rot",
        "img": "../../static/fruit_app/img/kirsche.jpg",
    },
    {
        "name": "Ananas",
        "gewicht": 1000,
        "farbe": "Gelb",
        "img": "../../static/fruit_app/img/ananas.jpg",
    },
]
