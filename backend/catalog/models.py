from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.category_name


from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    color = models.CharField(max_length=8)
    height = models.IntegerField()
    width = models.IntegerField()
    length = models.IntegerField()

    category = models.ForeignKey(
        "catalog.Category",
        on_delete=models.PROTECT,
        related_name="products",
    )

    location = models.ForeignKey(
        "stock.WarehouseLocation",
        on_delete=models.PROTECT,
        related_name="products",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "product"

class ProductImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE,
        related_name="images",
    )
    image_url = models.CharField(max_length=500)
    is_primary = models.BooleanField(default=False)

    class Meta:
        db_table = "product_image"

    def __str__(self):
        return f"Image for {self.product.product_name}"