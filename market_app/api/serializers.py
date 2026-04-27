from rest_framework import serializers  # type: ignore

from market_app.models import Market, Product, Seller


class MarketSerializer(serializers.ModelSerializer):
    sellers = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Market
        fields = "__all__"


class MarketHyperlinkedModelSerializer(
    MarketSerializer, serializers.HyperlinkedModelSerializer
):
    def __init__(self, *args, **kwargs):  # type: ignore
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)  # type: ignore

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)  # type: ignore

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)  # type: ignore
            existing = set(self.fields)  # type: ignore
            for field_name in existing - allowed:  # type: ignore
                self.fields.pop(field_name)  # type: ignore

    class Meta:  # type: ignore
        model = Market
        # exclude = []
        fields = ["id", "url", "name", "location", "description", "net_worth"]


class SellerSerializer(serializers.ModelSerializer):
    # Relationship to markets
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(), many=True, write_only=True, source="markets"
    )

    market_count = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = ["id", "name", "market_ids", "market_count", "markets", "contact_info"]

    def get_market_count(self, obj):
        return obj.markets.count()


class SellerHyperlinkedModelSerializer(
    SellerSerializer, serializers.HyperlinkedModelSerializer
):
    class Meta:  # type: ignore
        model = Seller
        fields = [
            "id",
            "url",
            "name",
            "market_ids",
            "market_count",
            "markets",
            "contact_info",
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "market", "seller"]


class ProductHyperlinkedModelSerializer(
    ProductSerializer, serializers.HyperlinkedModelSerializer
):
    class Meta:  # type: ignore
        model = Product
        fields = ["id", "url", "name", "description", "price", "market", "seller"]
