from rest_framework import routers

from .views import (
    MarketsViewSet,
    ProductsViewSet,
    SellersViewSet,
)

router = routers.SimpleRouter()
router.register(r"markets", MarketsViewSet)
router.register(r"sellers", SellersViewSet)
router.register(r"products", ProductsViewSet)

urlpatterns = router.urls
