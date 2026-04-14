from django.http import HttpRequest, JsonResponse
from django.shortcuts import render


def send_fruits(request: HttpRequest):
    # Hier passiert der Fehler ohne safe=False
    return JsonResponse(fruits, safe=False)


def send_fruits_template(request: HttpRequest | None):
    context: dict[str, list[dict[str, str | int | bool]]] = {"fruits": fruits}
    return render(request, "fruit_app/fruitlist.html", context)


def fruit_info(request: HttpRequest | None):
    return render(request, "fruit_app/info.html", fruits[0])


fruits: list[dict[str, str | int | bool]] = [
    {
        "name": "Apfel",
        "gewicht": 150,
        "farbe": "Rot",
        "img": "../../static/fruit_app/img/apfel.webp",
        "is_ordered": True,
    },
    {
        "name": "Banane",
        "gewicht": 120,
        "farbe": "Gelb",
        "img": "../../static/fruit_app/img/banane.jpg",
        "is_ordered": False,
    },
    {
        "name": "Orange",
        "gewicht": 200,
        "farbe": "Orange",
        "img": "../../static/fruit_app/img/orange.jpg",
        "is_ordered": True,
    },
    {
        "name": "Kirsche",
        "gewicht": 10,
        "farbe": "Rot",
        "img": "../../static/fruit_app/img/kirsche.jpg",
        "is_ordered": False,
    },
    {
        "name": "Ananas",
        "gewicht": 1000,
        "farbe": "Gelb",
        "img": "../../static/fruit_app/img/ananas.jpg",
        "is_ordered": True,
    },
]
