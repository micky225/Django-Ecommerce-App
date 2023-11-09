from Ecommerce_Console.basemodel import TimeBaseModel
from django.db import models

class Product(TimeBaseModel):
    name = models.CharField(max_length=100)
    was_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    price =  models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0)
    image = models.ImageField(null=True, blank=True)



    @property 
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 