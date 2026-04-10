from rest_framework import viewsets, filters

from .models import (
    Supplier,
    Warehouse,
    WarehouseLocation,
    RestockOrder,
    RestockDetail,
)
from .serializers import (
    SupplierSerializer,
    WarehouseSerializer,
    WarehouseLocationSerializer,
    RestockOrderSerializer,
    RestockDetailSerializer,
)


class SupplierViewSet(viewsets.ModelViewSet):
    """
    Enable admin CRUD for suppliers.
    Existing frontend can still use GET /api/stock/suppliers/
    but now POST, PUT, PATCH, DELETE also work.
    """

    queryset = Supplier.objects.all().order_by("supplier_id")
    serializer_class = SupplierSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["company_name", "contact_person", "phone_num", "address"]
    ordering_fields = ["supplier_id", "company_name", "contact_person"]


class WarehouseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Warehouse.objects.all().order_by("warehouse_id")
    serializer_class = WarehouseSerializer


class WarehouseLocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = (
        WarehouseLocation.objects.select_related("warehouse")
        .all()
        .order_by("location_id")
    )
    serializer_class = WarehouseLocationSerializer


class RestockOrderViewSet(viewsets.ModelViewSet):
    queryset = (
        RestockOrder.objects.select_related("supplier", "employee", "location")
        .prefetch_related("details__product")
        .all()
        .order_by("restock_id")
    )
    serializer_class = RestockOrderSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "supplier__company_name",
        "employee__efirst_name",
        "employee__elast_name",
        "restock_status",
    ]
    ordering_fields = ["restock_id", "restock_date", "restock_status"]


class RestockDetailViewSet(viewsets.ModelViewSet):
    queryset = (
        RestockDetail.objects.select_related("restock", "product")
        .all()
        .order_by("restock_detail_id")
    )
    serializer_class = RestockDetailSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["product__product_name", "restock__restock_status"]
    ordering_fields = ["restock_detail_id", "quantity", "restock"]

