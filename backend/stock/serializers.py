from rest_framework import serializers
from .models import Supplier, Warehouse, WarehouseLocation, RestockOrder, RestockDetail


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            "supplier_id",
            "company_name",
            "contact_person",
            "phone_num",
            "address",
        ]


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            "warehouse_id",
            "wname",
            "wphone",
            "waddress",
        ]


class WarehouseLocationSerializer(serializers.ModelSerializer):
    warehouse_name = serializers.CharField(source="warehouse.wname", read_only=True)

    class Meta:
        model = WarehouseLocation
        fields = [
            "location_id",
            "warehouse",
            "warehouse_name",
            "aisle",
            "zone",
            "bin",
        ]


class RestockDetailSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.product_name", read_only=True)

    class Meta:
        model = RestockDetail
        fields = [
            "restock_detail_id",
            "restock",
            "product",
            "product_name",
            "quantity",
        ]


class RestockOrderSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source="supplier.company_name", read_only=True)
    employee_name = serializers.SerializerMethodField()
    location_name = serializers.SerializerMethodField()
    details = RestockDetailSerializer(many=True, read_only=True)

    class Meta:
        model = RestockOrder
        fields = [
            "restock_id",
            "supplier",
            "supplier_name",
            "employee",
            "employee_name",
            "location",
            "location_name",
            "restock_date",
            "restock_status",
            "details",
        ]

    def get_employee_name(self, obj):
        return f"{obj.employee.efirst_name} {obj.employee.elast_name}"

    def get_location_name(self, obj):
        return str(obj.location)