from django.urls import include, path
from rest_framework import routers  # type: ignore

from .views import (
    MarketsViewSet,
    ProductsViewSet,
    SellersViewSet,
)

router = routers.SimpleRouter()
router.register(r"markets", MarketsViewSet)  # type: ignore
router.register(r"sellers", SellersViewSet)  # type: ignore
router.register(r"products", ProductsViewSet)  # type: ignore

urlpatterns = [
    path("", include(router.urls)),  # type: ignore
]
