from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListAPIView

from .models import Product, Category, Pair
from .serializers import ProductSerializer, CategorySerializer, PairSerializer


class ProductView(ListAPIView, ViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.prefetch_related("categories").all()
        return queryset.all()


class CategoryView(ListAPIView, ViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.prefetch_related("products")
        return queryset.all()


class PairsView(ListAPIView, ViewSet):
    serializer_class = PairSerializer

    def get_queryset(self):
        return Pair.objects.select_related("product").select_related("categories").all()
