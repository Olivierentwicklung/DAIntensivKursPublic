from django.http import JsonResponse

# Create your views here.


def send_fruits(request: str):
    fruits: list[dict[str, str | int]] = [
        {"name": "Apfel", "gewicht": 150, "farbe": "Rot"},
        {"name": "Banane", "gewicht": 120, "farbe": "Gelb"},
        {"name": "Orange", "gewicht": 200, "farbe": "Orange"},
        {"name": "Kirsche", "gewicht": 10, "farbe": "Rot"},
        {"name": "Ananas", "gewicht": 1000, "farbe": "Gelb"},
    ]
    return JsonResponse(fruits)
