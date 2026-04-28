from rest_framework import serializers

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
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:  # type: ignore
        model = Market
        # exclude = []
        fields = [
            "id",
            "url",
            "name",
            "location",
            "description",
            "net_worth",
            "image_url",
        ]


class SellerSerializer(serializers.ModelSerializer):
    # Relationship to markets
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(), many=True, write_only=True, source="markets"
    )

    market_count = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = [
            "id",
            "name",
            "market_ids",
            "market_count",
            "markets",
            "contact_info",
            "image_url",
        ]

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
            "image_url",
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "market",
            "seller",
            "image_url",
        ]


class ProductHyperlinkedModelSerializer(
    ProductSerializer, serializers.HyperlinkedModelSerializer
):
    class Meta:  # type: ignore
        model = Product
        fields = [
            "id",
            "url",
            "name",
            "description",
            "price",
            "market",
            "seller",
            "image_url",
        ]
