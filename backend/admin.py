from django.contrib import admin
from backend.models.products import Product
from backend.models.order_items import OrderItem

# Register your models here.

admin.site.register(Product)
admin.site.register(OrderItem)