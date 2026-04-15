from django.http import HttpRequest, JsonResponse
from django.shortcuts import render


def send_fruits(request: HttpRequest):
    # Hier passiert der Fehler ohne safe=False
    return JsonResponse(fruits, safe=False)


def send_fruits_template(request: HttpRequest | None):
    context = transform_list_into_dict("fruits", fruits)
    return render(request, "fruit_app/fruitlist.html", context)


def fruit_info(request: HttpRequest | None):
    context = transform_list_into_dict("fruits", fruits)
    return render(request, "fruit_app/info.html", context)


def transform_list_into_dict(
    key: str,
    list: list[dict[str, str | int | bool | dict[str, str | list[str]]]],
) -> dict[str, list[dict[str, str | int | bool | dict[str, str | list[str]]]]]:
    return {key: list}


fruits: list[dict[str, str | int | bool | dict[str, str | list[str]]]] = [
    {
        "name": "Apfel",
        "gewicht": 150,
        "farbe": "Rot",
        "img": "fruit_app/img/apfel.webp",
        "is_ordered": True,
        "infos": {
            "title": "Apple – Sweet & Crisp Variety",
            "description": "Apples are crunchy, refreshing fruits that support digestion and overall health. They are perfect for snacks and help keep you feeling full longer.",
            "vitamins": ["Vitamin C", "Vitamin K", "Vitamin B6"],
        },
    },
    {
        "name": "Banane",
        "gewicht": 120,
        "farbe": "Gelb",
        "img": "fruit_app/img/banane.jpg",
        "is_ordered": False,
        "infos": {
            "title": "Banana – Soft & Energy-Rich Variety",
            "description": "Bananas are soft, naturally sweet fruits that provide quick energy and support muscle function, making them ideal for active lifestyles.",
            "vitamins": ["Vitamin B6 ", "Vitamin C", "Folate (Vitamin B9)"],
        },
    },
    {
        "name": "Orange",
        "gewicht": 200,
        "farbe": "Orange",
        "img": "fruit_app/img/orange.jpg",
        "is_ordered": True,
        "infos": {
            "title": "Orange – Juicy Citrus Variety",
            "description": "Oranges are juicy and refreshing citrus fruits known for boosting the immune system and keeping your body hydrated.",
            "vitamins": ["Vitamin C", "Vitamin A", "Vitamin B1"],
        },
    },
    {
        "name": "Kirsche",
        "gewicht": 10,
        "farbe": "Rot",
        "img": "fruit_app/img/kirsche.jpg",
        "is_ordered": False,
        "infos": {
            "title": "Cherry – Small & Antioxidant-Rich Variety",
            "description": "Cherries are small, juicy fruits packed with antioxidants that help reduce inflammation and support better sleep and recovery.",
            "vitamins": ["Vitamin C", "Vitamin A", "Vitamin F"],
        },
    },
    {
        "name": "Ananas",
        "gewicht": 1000,
        "farbe": "Gelb",
        "img": "fruit_app/img/ananas.jpg",
        "is_ordered": True,
        "infos": {
            "title": "Pineapple – Tropical Sweet-Tart Variety",
            "description": "Pineapples have a unique sweet and tangy flavor and contain enzymes that aid digestion while providing a tropical refreshment.",
            "vitamins": ["Vitamin C", "Vitamin B6", "Vitamin A1"],
        },
    },
]
