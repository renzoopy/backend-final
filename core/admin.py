from django.contrib import admin

# Register your models here.

from core.models import Product, Client, ProductDetail, ProductSale


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name", "price", "stocks")
    list_display_links = ("id", "name")
    ordering = ("name",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "ruc", "name", "email")
    list_display_links = ("id", "name")
    ordering = ("name",)


@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "product_sale", "stocks", "total")
    list_display_links = ("id", "product")
    ordering = ("product",)


@admin.register(ProductSale)
class ProductSaleAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "invoice", "client", "total")
    list_display_links = ("id", "invoice")
    ordering = ("invoice",)
