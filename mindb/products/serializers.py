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
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["uuid", "name", "products"]

    def get_products(self, instance):

        products = Product.objects.filter(categories__uuid=instance.uuid)

        return ProductForCategorySerializer(
            products,
            many=True,
        ).data


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
