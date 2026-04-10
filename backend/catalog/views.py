from rest_framework import viewsets, filters

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by("category_id")
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    Enable admin CRUD for products.
    Read APIs remain compatible with the current frontend.
    """

    queryset = (
        Product.objects.select_related("category", "location")
        .prefetch_related("images")
        .all()
        .order_by("product_id")
    )
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["product_name", "color", "category__category_name"]
    ordering_fields = ["price", "stock_quantity", "product_name", "product_id"]

