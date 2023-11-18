from Ecommerce_Console.basemodel import TimeBaseModel
from django.db import models
from backend.models.products import Product

class OrderItem(TimeBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity 
        return total 

    def __str__(self):
        return str(self.id)