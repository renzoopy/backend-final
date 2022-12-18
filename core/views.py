from rest_framework import viewsets

from core.filters import ProductSaleFilter
from core.models import Product, Client, ProductDetail, ProductSale
from core.serializers import (
    ProductDetailSerializer,
    ProductSaleViewSerializer,
    ProductSerializer,
    ClientSerializer,
    ProductSaleSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer
    # filterset_class = FamilyMemberFilter


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by("id")
    serializer_class = ClientSerializer
    # filterset_class = FamilyMemberFilter


class ProductSaleViewSet(viewsets.ModelViewSet):
    queryset = ProductSale.objects.all().order_by("date", "client")
    serializer_class = ProductSaleSerializer
    filterset_class = ProductSaleFilter

    def get_serializer_class(self):
        if self.action == "list":
            return ProductSaleViewSerializer
        return self.serializer_class


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all().order_by("id")
    serializer_class = ProductDetailSerializer
    # filterset_class = FamilyMemberFilter
