from django.urls import path

from .views import (
    MarketDetail,
    MarketsView,
    SellersView,
    product_single_view,
    products_view,
    seller_single_view,
)

urlpatterns = [
    path("market/", MarketsView.as_view()),
    path("market/<int:pk>/", MarketDetail.as_view(), name="market-detail"),
    path("seller/", SellersView.as_view()),
    path("seller/<int:pk>/", seller_single_view, name="seller-detail"),
    path("product/", products_view),
    path("product/<int:pk>/", product_single_view, name="product-detail"),
]
