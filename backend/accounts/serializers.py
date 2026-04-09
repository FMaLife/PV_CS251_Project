from rest_framework import serializers
from .models import Customer, CustomerAddress, Employee


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = [
            "address_id",
            "customer",
            "address_type",
            "house_no",
            "street",
            "subdistrict",
            "district",
            "province",
            "zip_code",
        ]


class CustomerSerializer(serializers.ModelSerializer):
    addresses = CustomerAddressSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = [
            "customer_id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "addresses",
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = [
            "employee_id",
            "efirst_name",
            "elast_name",
            "full_name",
            "ephone",
            "eemail",
            "role",
        ]

    def get_full_name(self, obj):
        return f"{obj.efirst_name} {obj.elast_name}"