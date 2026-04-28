from decimal import Decimal

from django.core.management.base import BaseCommand

from market_app.models import Market, Product, Seller

# in Terminal: python manage.py seed_market_app


class Command(BaseCommand):
    help = "Seed database with dummy markets, sellers and products"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Seller.objects.all().delete()
        Market.objects.all().delete()

        markets = [
            Market.objects.create(
                name="Central Market",
                location="Berlin",
                description="A large city market with many local sellers.",
                net_worth=Decimal("250000.00"),
                image_url="https://images.unsplash.com/photo-1546726747-421c6d69c929?w=800",
            ),
            Market.objects.create(
                name="Fresh Food Market",
                location="Hamburg",
                description="A fresh food market with vegetables, fruits and snacks.",
                net_worth=Decimal("180000.00"),
                image_url="https://media.istockphoto.com/id/2225367775/photo/st-pauli-landungsbruecken-in-hamburg-during-daytime.webp?a=1&b=1&s=612x612&w=0&k=20&c=JUm0lVm_O3_VPJSysKl7DPli_1EwvdRwpjav69MD5to=",
            ),
            Market.objects.create(
                name="Weekend Bazaar",
                location="Munich",
                description="A weekend market for handmade products and food.",
                net_worth=Decimal("120000.00"),
                image_url="https://images.unsplash.com/photo-1734567112080-ef59a3fa9763?w=800",
            ),
        ]

        sellers = [
            Seller.objects.create(
                name="Anna Müller",
                contact_info="anna@example.com",
                image_url="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=800",
            ),
            Seller.objects.create(
                name="Omar Khan",
                contact_info="omar@example.com",
                image_url="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800",
            ),
            Seller.objects.create(
                name="Oliver Smith",
                contact_info="oliver@example.com",
                image_url="https://media.istockphoto.com/id/1138563417/photo/african-american-businessman-smiling-on-grey.webp?a=1&b=1&s=612x612&w=0&k=20&c=tg6nEL4JnPjE8q4bK3kWsKMcEL7QeUYBa5ntH4kKi98=",
            ),
        ]

        sellers[0].markets.add(markets[0], markets[1])
        sellers[1].markets.add(markets[0], markets[2])
        sellers[2].markets.add(markets[1], markets[2])

        products = [
            {
                "name": "Organic Apples",
                "description": "Fresh organic apples from local farms.",
                "price": "3.99",
                "market": markets[0],
                "seller": sellers[0],
                "image_url": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=800",
            },
            {
                "name": "Fresh Tomatoes",
                "description": "Red and juicy tomatoes.",
                "price": "2.49",
                "market": markets[1],
                "seller": sellers[0],
                "image_url": "https://images.unsplash.com/photo-1582284540020-8acbe03f4924?w=800",
            },
            {
                "name": "Handmade Bread",
                "description": "Freshly baked handmade bread.",
                "price": "4.50",
                "market": markets[0],
                "seller": sellers[1],
                "image_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=800",
            },
            {
                "name": "Flower Bouquet",
                "description": "Colorful flowers for decoration.",
                "price": "12.99",
                "market": markets[2],
                "seller": sellers[1],
                "image_url": "https://images.unsplash.com/photo-1490750967868-88aa4486c946?w=800",
            },
            {
                "name": "Cheese Selection",
                "description": "Different types of fresh cheese.",
                "price": "8.99",
                "market": markets[1],
                "seller": sellers[2],
                "image_url": "https://images.unsplash.com/photo-1452195100486-9cc805987862?w=800",
            },
            {
                "name": "Strawberries",
                "description": "Sweet strawberries in a basket.",
                "price": "5.99",
                "market": markets[2],
                "seller": sellers[2],
                "image_url": "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?w=800",
            },
        ]

        for product in products:
            Product.objects.create(
                name=product["name"],
                description=product["description"],
                price=Decimal(product["price"]),
                market=product["market"],
                seller=product["seller"],
                image_url=product["image_url"],
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
