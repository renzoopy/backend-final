import django_filters
from core.models import ProductSale


class ProductSaleFilter(django_filters.FilterSet):
    date_min = django_filters.DateFilter(
        field_name="date",
        lookup_expr="gte",
        label="Creation Date Min",
    )
    date_max = django_filters.DateFilter(
        field_name="date",
        lookup_expr="lte",
        label="Creation Date Max",
    )

    class Meta:
        model = ProductSale
        fields = (
            "date_min",
            "date_max",
            "client",
            "products",
        )
