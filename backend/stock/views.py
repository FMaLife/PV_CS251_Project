from rest_framework import viewsets
from .models import Supplier, Warehouse, WarehouseLocation, RestockOrder, RestockDetail
from .serializers import (
    SupplierSerializer,
    WarehouseSerializer,
    WarehouseLocationSerializer,
    RestockOrderSerializer,
    RestockDetailSerializer,
)


class SupplierViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Supplier.objects.all().order_by("supplier_id")
    serializer_class = SupplierSerializer


class WarehouseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Warehouse.objects.all().order_by("warehouse_id")
    serializer_class = WarehouseSerializer


class WarehouseLocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WarehouseLocation.objects.select_related("warehouse").all().order_by("location_id")
    serializer_class = WarehouseLocationSerializer


class RestockOrderViewSet(viewsets.ModelViewSet):
    queryset = (
        RestockOrder.objects.select_related("supplier", "employee", "location")
        .prefetch_related("details__product")
        .all()
        .order_by("restock_id")
    )
    serializer_class = RestockOrderSerializer


class RestockDetailViewSet(viewsets.ModelViewSet):
    queryset = RestockDetail.objects.select_related("restock", "product").all().order_by("restock_detail_id")
    serializer_class = RestockDetailSerializer