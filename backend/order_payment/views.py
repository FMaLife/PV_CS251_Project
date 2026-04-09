from rest_framework import viewsets
from .models import SaleOrder, OrderDetail, Payment
from .serializers import SaleOrderSerializer, OrderDetailSerializer, PaymentSerializer


class SaleOrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = (
        SaleOrder.objects.select_related("customer", "owner")
        .prefetch_related("details__product")
        .select_related("payment")
        .all()
        .order_by("order_id")
    )
    serializer_class = SaleOrderSerializer


class OrderDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrderDetail.objects.select_related("order", "product").all().order_by("line_number")
    serializer_class = OrderDetailSerializer


class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Payment.objects.select_related("order").all().order_by("ref_number")
    serializer_class = PaymentSerializer