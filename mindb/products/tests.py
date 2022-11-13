from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from .models import Product, Category, Pair
from .serializers import ProductSerializer, CategorySerializer, PairSerializer


client = Client()


class ProductTest(TestCase):
    fixtures = [
        "mindb/fixtures/products-fixture.json",
    ]

    def test_product(self):
        response = client.get(reverse("products:product-list"))
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CategoryTest(TestCase):
    fixtures = [
        "mindb/fixtures/products-fixture.json",
    ]

    def test_product(self):
        response = client.get(reverse("products:category-list"))
        product = Category.objects.all()
        serializer = CategorySerializer(product, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PairTest(TestCase):
    fixtures = [
        "mindb/fixtures/products-fixture.json",
    ]

    def test_product(self):
        response = client.get(reverse("products:pair-list"))
        product = Pair.objects.all()
        serializer = PairSerializer(product, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
