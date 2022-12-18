from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Product, Client, ProductDetail, ProductSale


class Command(BaseCommand):
    def handle(self, *args, **options):

        ###! Creando superusuario
        print("Creando superusuario")
        user = User.objects.create(
            username="admin",
            email="admin@admin.com",
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )
        user.set_password("Cuaderno.1")
        user.save()

        ###! Creando Clientes
        print("Creando Clientes")
        client = Client.objects.create(
            ruc="4177075-4",
            name="Lorenzo Cabrera",
            email="lorenzo@admin.com",
        )
        client.save()

        client = Client.objects.create(
            ruc="1722607-4",
            name="Nancy Villamayor",
            email="nancy@admin.com",
        )
        client.save()

        clients = []
        for client in Client.objects.all():
            clients.append(client)

        ###! Creando Productos
        print("Creando Productos")
        product = Product.objects.create(
            code="001-A",
            name="Leche",
            price=3000,
            stocks=10,
        )
        product.save()
        product = Product.objects.create(
            code="002-A",
            name="Pollo",
            price=18000,
            stocks=10,
        )
        product.save()
        product = Product.objects.create(
            code="001-B",
            name="Caja de leche",
            price=26000,
            stocks=10,
        )
        product.save()

        products = []
        for product in Product.objects.all():
            products.append(product)

        ###! Creando ventas
        print("Creando detalles de ventas")
        sale = ProductSale.objects.create(
            date="2022-12-3",
            invoice="AAA1515",
            total=0,
            client=clients[0],
        )
        sale.save()
        sale = ProductSale.objects.create(
            date="2022-12-25",
            invoice="GYL1623",
            total=0,
            client=clients[1],
        )
        sale.save()
        sales = []
        for sale in ProductSale.objects.all():
            sales.append(sale)

        # ###! Creaando detalles de ventas
        # detail = ProductDetail.objects.create(
        #     product=products[0],
        #     product_sale=sales[0],
        #     stocks=1,
        # )
        # detail.save()
        # detail = ProductDetail.objects.create(
        #     product=products[1],
        #     product_sale=sales[0],
        #     stocks=2,
        # )
        # detail.save()
