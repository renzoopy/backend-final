from rest_framework import serializers
from core.models import Product, ProductDetail, ProductSale, Client


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "code",
            "name",
            "price",
            "stocks",
            "created_at",
            "updated_at",
        )

    def validate_name(self, value):
        if not self.instance and Product.objects.filter(name=value).exists():
            raise serializers.ValidationError("Un producto con ese nombre ya existe")
        return value

    def validate_code(self, value):
        if not self.instance and Product.objects.filter(code=value).exists():
            raise serializers.ValidationError("Un producto con ese codigo ya existe")
        return value


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "ruc",
            "name",
            "email",
            "created_at",
            "updated_at",
        )

    def validate_ruc(self, value):
        if not self.instance and Client.objects.filter(ruc=value).exists():
            raise serializers.ValidationError(
                "Un cliente con ese número de RUC ya existe"
            )
        return value

    def validate_email(self, value):
        if not self.instance and Client.objects.filter(email=value).exists():
            raise serializers.ValidationError("Un cliente con ese mail ya existe")
        return value


class SaleProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    detail_id = id
    product_id = serializers.IntegerField(source="product.id")
    product_name = serializers.CharField(source="product.name", max_length=100)
    product_stocks = serializers.IntegerField(source="product.stocks")
    product_price = serializers.FloatField(source="product.price")
    stocks_total = serializers.IntegerField(source="stocks")
    sale_total = serializers.IntegerField(source="total")


class ProductSaleSerializer(serializers.ModelSerializer):
    products = SaleProductSerializer(many=True, source="details", read_only=True)

    class Meta:
        model = ProductSale
        fields = (
            "id",
            "date",
            "invoice",
            "client",
            "products",
            "created_at",
            "updated_at",
        )


class ProductSaleViewSerializer(serializers.ModelSerializer):
    products = SaleProductSerializer(many=True, source="details", read_only=True)

    class Meta:
        model = ProductSale
        fields = (
            "id",
            "date",
            "invoice",
            "client",
            "products",
            "total",
            "created_at",
            "updated_at",
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = (
            "id",
            "product",
            "product_sale",
            "stocks",
        )

    def create(self, validated_data):
        product = validated_data.get("product", None)
        stocks = validated_data.get("stocks", None)

        if product.stocks < stocks:
            raise serializers.ValidationError(
                "No existen suficientes existencias del producto."
            )
        product.stocks -= stocks
        product.save()
        price = product.price * stocks
        validated_data["total"] = price

        sale = validated_data.get("product_sale", None)
        sale.total += price
        sale.save()
        return super().create(validated_data)
