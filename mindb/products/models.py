import uuid
from django.db import models


class Pair(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, blank=True)
    categories = models.ForeignKey("Category", on_delete=models.CASCADE,  blank=True)


class Product(models.Model):
    uuid = models.UUIDField(
        "id",
        primary_key=True,
        default=uuid.uuid4,
    )
    name = models.CharField("наименование", max_length=255, db_index=True)
    categories = models.ManyToManyField("Category", verbose_name="категории", blank=True, through=Pair)

    def __str__(self):
        return f"{self.name}: {self.uuid}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Category(models.Model):
    uuid = models.UUIDField(
        "id",
        primary_key=True,
        default=uuid.uuid4,
    )
    name = models.CharField("наименование", max_length=255, db_index=True)

    def __str__(self):
        return f"{self.name}: {self.uuid}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



