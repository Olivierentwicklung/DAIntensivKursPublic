from rest_framework import viewsets  # type: ignore

from market_app.models import Market, Product, Seller

from .serializers import (
    MarketHyperlinkedModelSerializer,
    ProductHyperlinkedModelSerializer,
    SellerHyperlinkedModelSerializer,
)


class MarketsViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketHyperlinkedModelSerializer


class SellersViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerHyperlinkedModelSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductHyperlinkedModelSerializer
