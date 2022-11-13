from django.contrib import admin

from .models import Product, Category, Pair


class PairInline(admin.TabularInline):
    model = Pair
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (PairInline,)
    list_display = [
        "uuid",
        "name",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (PairInline,)
    list_display = [
        "uuid",
        "name",
    ]



