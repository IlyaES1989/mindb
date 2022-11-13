from rest_framework import serializers

from .models import Product, Category, Pair


class ProductForCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["uuid", "name"]


class CategoryForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["uuid", "name"]


class CategorySerializer(serializers.ModelSerializer):
    products = ProductForCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ["uuid", "name", "products"]


class ProductSerializer(serializers.ModelSerializer):
    categories = CategoryForProductSerializer(
        many=True,
    )

    class Meta:
        model = Product
        fields = ["uuid", "name", "categories"]


class PairSerializer(serializers.ModelSerializer):
    product = ProductForCategorySerializer()
    categories = CategoryForProductSerializer()

    class Meta:
        model = Pair
        fields = ["product", "categories"]
