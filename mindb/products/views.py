from rest_framework.viewsets import ModelViewSet

from .models import Product, Category, Pair
from .serializers import ProductSerializer, CategorySerializer, PairSerializer


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.prefetch_related("categories")
        return queryset.all()


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.prefetch_related("products")
        return queryset.all()


class PairsView(ModelViewSet):
    serializer_class = PairSerializer

    def get_queryset(self):
        return Pair.objects.select_related("product").select_related("categories").all()
