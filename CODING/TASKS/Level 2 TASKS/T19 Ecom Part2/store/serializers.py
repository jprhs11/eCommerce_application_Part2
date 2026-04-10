from rest_framework import serializers
from .models import Store, Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "content",
            "rating",
            "is_verified",
            "created_at",
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "stock", "store"]


class StoreSerializer(serializers.ModelSerializer):
    # This allows us to see products and reviews nested inside the store JSON
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ["id", "name", "description", "vendor", "products"]
        read_only_fields = [
            "vendor"
        ]  # Vendor is set automatically from the request
