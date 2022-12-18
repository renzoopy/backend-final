from django.urls import path, conf

from rest_framework.routers import DefaultRouter

from core.views import (
    ProductDetailViewSet,
    ProductViewSet,
    ClientViewSet,
    ProductSaleViewSet,
)

router = DefaultRouter()

router.register("products", ProductViewSet, basename="products")
router.register("clients", ClientViewSet, basename="clients")
router.register("product-sales", ProductSaleViewSet, basename="product-sales")
router.register("product-details", ProductDetailViewSet, basename="product-details")

urlpatterns = [path("", conf.include(router.urls))]
