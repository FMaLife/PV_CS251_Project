from django.db import models


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer = models.OneToOneField(
        "accounts.Customer",
        on_delete=models.CASCADE,
        related_name="cart",
    )
    create_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "cart"

    def __str__(self):
        return f"Cart #{self.cart_id}"


class CartItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(
        "cart_delivery.Cart",
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.PROTECT,
        related_name="cart_items",
    )
    quantity = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)
    cartitem_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        db_table = "cart_item"
        unique_together = ("cart", "product")

    def __str__(self):
        return f"{self.product.product_name} x {self.quantity}"

    def save(self, *args, **kwargs):
        self.cartitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    order = models.OneToOneField(
        "order_payment.SaleOrder",
        on_delete=models.CASCADE,
        related_name="delivery",
    )
    address = models.ForeignKey(
        "accounts.CustomerAddress",
        on_delete=models.PROTECT,
        related_name="deliveries",
    )
    tracking_number = models.CharField(max_length=13, blank=True, null=True)
    delivery_name = models.CharField(max_length=150, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "delivery"

    def __str__(self):
        return f"Delivery for order {self.order_id}"