from rest_framework import serializers

from .models import Category, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category_id", "category_name"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image_id", "image_url", "is_primary"]


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.category_name", read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "product_id",
            "product_name",
            "price",
            "stock_quantity",
            "color",
            "height",
            "width",
            "length",
            "category",
            "category_name",
            "location",
            "images",
        ]
        read_only_fields = ["product_id", "category_name", "images"]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("price cannot be negative")
        return value

    def validate_stock_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("stock_quantity cannot be negative")
        return value

    def validate(self, attrs):
        for field_name in ("height", "width", "length"):
            value = attrs.get(field_name)
            if value is not None and value <= 0:
                raise serializers.ValidationError(
                    {field_name: f"{field_name} must be greater than 0"}
                )
        return attrs

