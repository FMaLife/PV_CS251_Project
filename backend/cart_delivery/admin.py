from django.contrib import admin
from .models import Cart, CartItem, Delivery

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Delivery)