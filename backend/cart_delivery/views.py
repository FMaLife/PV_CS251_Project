from rest_framework import viewsets
from .models import Cart, CartItem, Delivery
from .serializers import CartSerializer, CartItemSerializer, DeliverySerializer


class CartViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cart.objects.prefetch_related("items__product").all().order_by("cart_id")
    serializer_class = CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.select_related("cart", "product").all().order_by("item_id")
    serializer_class = CartItemSerializer


class DeliveryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Delivery.objects.select_related("order", "address").all().order_by("delivery_id")
    serializer_class = DeliverySerializer