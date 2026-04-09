from rest_framework import serializers
from .models import SaleOrder, OrderDetail, Payment


class OrderDetailSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.product_name", read_only=True)

    class Meta:
        model = OrderDetail
        fields = [
            "line_number",
            "order",
            "product",
            "product_name",
            "quantity",
            "subtotal",
        ]
        read_only_fields = ["line_number", "subtotal"]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "ref_number",
            "order",
            "locked_amount",
            "payment_status",
            "payment_timestamp",
        ]


class SaleOrderSerializer(serializers.ModelSerializer):
    details = OrderDetailSerializer(many=True, read_only=True)
    payment = PaymentSerializer(read_only=True)
    owner_name = serializers.SerializerMethodField()

    class Meta:
        model = SaleOrder
        fields = [
            "order_id",
            "customer",
            "owner",
            "owner_name",
            "order_date",
            "order_status",
            "total_amount",
            "details",
            "payment",
        ]

    def get_owner_name(self, obj):
        if not obj.owner:
            return None
        return f"{obj.owner.efirst_name} {obj.owner.elast_name}"