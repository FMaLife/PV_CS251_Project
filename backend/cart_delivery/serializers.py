from rest_framework import serializers
from .models import Cart, CartItem, Delivery


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.product_name", read_only=True)
    product_price = serializers.DecimalField(
        source="product.price",
        max_digits=12,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = CartItem
        fields = [
            "item_id",
            "cart",
            "product",
            "product_name",
            "product_price",
            "quantity",
            "added_date",
            "cartitem_total",
        ]
        read_only_fields = ["item_id", "added_date", "cartitem_total"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = [
            "cart_id",
            "customer",
            "create_date",
            "last_updated",
            "items",
        ]
        read_only_fields = ["cart_id", "create_date", "last_updated"]


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = [
            "delivery_id",
            "order",
            "address",
            "tracking_number",
            "delivery_name",
            "delivery_date",
        ]