from rest_framework.viewsets import ModelViewSet

from .models import Product, Category, Pair
from .serializers import ProductSerializer, CategorySerializer, PairSerializer


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class PairsView(ModelViewSet):
    serializer_class = PairSerializer

    def get_queryset(self):
        return Pair.objects.all()
