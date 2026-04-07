from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    class Meta:
        db_table = "customer"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Employee(models.Model):
    class RoleChoices(models.TextChoices):
        ADMIN = "Admin", "Admin"
        STAFF = "Staff", "Staff"

    employee_id = models.AutoField(primary_key=True)
    efirst_name = models.CharField(max_length=100)
    elast_name = models.CharField(max_length=100)
    ephone = models.CharField(max_length=20)
    eemail = models.EmailField(max_length=100, unique=True)
    epassword = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=RoleChoices.choices)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return f"{self.efirst_name} {self.elast_name} ({self.role})"


class CustomerAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        "accounts.Customer",
        on_delete=models.CASCADE,
        related_name="addresses",
    )
    address_type = models.CharField(max_length=50)
    house_no = models.CharField(max_length=20)
    street = models.CharField(max_length=50, blank=True, null=True)
    subdistrict = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)

    class Meta:
        db_table = "customer_address"

    def __str__(self):
        return f"{self.address_type} - {self.customer.first_name}"