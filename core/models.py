from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    code = models.CharField(verbose_name=_("Código"), max_length=60)
    name = models.CharField(verbose_name=_("Nombre"), max_length=100)
    price = models.FloatField(verbose_name=_("Precio de venta"))
    stocks = models.IntegerField(verbose_name=_("Existencia"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Producto")
        verbose_name_plural = _("Productos")

    def __str__(self):
        return self.name


class Client(models.Model):
    ruc = models.CharField(verbose_name=_("RUC"), max_length=60)
    name = models.CharField(verbose_name=_("Nombre y apellido"), max_length=300)
    email = models.EmailField(verbose_name=_("Email"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Cliente")
        verbose_name_plural = _("Clientes")

    def __str__(self):
        return self.name


class ProductSale(models.Model):
    date = models.DateField(verbose_name=_("Fecha de venta"))
    invoice = models.CharField(verbose_name=_("Número de factura"), max_length=60)
    client = models.ForeignKey(
        Client,
        verbose_name=_("Cliente"),
        on_delete=models.CASCADE,
        related_name="productsales",
    )
    total = models.FloatField(verbose_name=_("Total"), null=True, blank=True)
    products = models.ManyToManyField(
        Product,
        through="ProductDetail",
        related_name="products",
        verbose_name=_("Productos"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Venta de productos")
        verbose_name_plural = _("Venta de productos")

    def __str__(self):
        return f"{self.invoice} - {self.client.name}"


class ProductDetail(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="details",
        verbose_name=_("Producto"),
    )
    product_sale = models.ForeignKey(
        ProductSale,
        on_delete=models.CASCADE,
        related_name="details",
        verbose_name=_("Venta de producto"),
    )
    stocks = models.IntegerField(verbose_name=_("Existencia"))
    total = models.FloatField(verbose_name=_("Total"), null=True, blank=True)

    class Meta:
        verbose_name = _("Detalle de producto")
        verbose_name_plural = _("Detalle de productos")

    def __str__(self):
        return f"{self.product.name} - {self.product_sale.invoice}"
