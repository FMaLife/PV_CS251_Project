from rest_framework import viewsets
from .models import Customer, CustomerAddress, Employee
from .serializers import CustomerSerializer, CustomerAddressSerializer, EmployeeSerializer


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.prefetch_related("addresses").all().order_by("customer_id")
    serializer_class = CustomerSerializer


class CustomerAddressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomerAddress.objects.select_related("customer").all().order_by("address_id")
    serializer_class = CustomerAddressSerializer


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all().order_by("employee_id")
    serializer_class = EmployeeSerializer