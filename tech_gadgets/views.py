from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from .dummy_data import gadgets, manufacturers


# Create your views here.
def start_page_view(request: HttpRequest | None):
    # return HttpResponse('hi!')
    # return render(request, 'tech_gadgets/test.html', {'gadgets_list': gadgets})

    context: dict[str, list[dict[str, str | int]] | list[dict[str, str | float]]] = {
        "gadgets": gadgets,
        "manufacturers": manufacturers,
        "smart_home": selectCategoriesByName("Smart Home"),
        "wearables": selectCategoriesByName("Wearable Technology"),
        "computers": selectCategoriesByName("Computer & Laptops"),
    }
    return render(request, "tech_gadgets/store.html", context)


def single_gadget_view(request: str):
    # return HttpResponse(json.dumps(gadgets[0]), content_type='application/json')
    return JsonResponse(gadgets[0])


def selectCategoriesByName(
    categoryName: str,
) -> list[dict[str, str | int]] | list[dict[str, str | float]]:
    """
    explain: [g for g in gadgets if g['category'] == 'Smart Home']
    This is equivalent to (It’s just a shorter way to filter a list.):
        result = []
        for g in gadgets:
            if g['category'] == 'Smart Home':
                result.append(g)
    """
    return [g for g in gadgets if g["category"] == categoryName]
