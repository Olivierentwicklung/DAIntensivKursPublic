from django.http import HttpRequest
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from market_app.models import Market, Product, Seller

from .serializers import (
    MarketHyperlinkedModelSerializer,
    MarketSerializer,
    ProductHyperlinkedModelSerializer,
    ProductSerializer,
    SellerSerializer,
)


class MarketsView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Market.objects.all()
    serializer_class = MarketHyperlinkedModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MarketDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SellersView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@api_view(["GET", "DELETE", "PUT"])
def seller_single_view(request: HttpRequest, pk: int):
    if request.method == "GET":
        seller = Seller.objects.get(pk=pk)
        serializer = SellerSerializer(seller, context={"request": request})
        return Response(serializer.data)

    if request.method == "PUT":
        seller = Seller.objects.get(pk=pk)
        serializer = SellerSerializer(seller, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == "DELETE":
        seller = Seller.objects.get(pk=pk)
        serializer = SellerSerializer(seller)
        seller.delete()
        return Response(serializer.data)


@api_view(["GET", "POST"])
def products_view(request: HttpRequest):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductHyperlinkedModelSerializer(
            products, many=True, context={"request": request}
        )
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(["GET", "DELETE", "PUT"])
def product_single_view(request: HttpRequest, pk: int):
    if request.method == "GET":
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, context={"request": request})
        return Response(serializer.data)

    if request.method == "PUT":
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == "DELETE":
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        product.delete()
        return Response(serializer.data)
