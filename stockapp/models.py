from django.db import models

# Create your models here.


class Product(models.Model):
    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=64)
    cost_price = models.FloatField(null=True, blank=True)
    sell_price = models.FloatField(null=True, blank=True)
    qty = models.PositiveIntegerField(default=0)


    def __str__():
    	return self.name




