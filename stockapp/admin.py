from django.contrib import admin

# Register your models here.
from .models import Product




class ProductAdmin(admin.ModelAdmin):
	list_display = ('code', 'name','cost_price', 'sell_price','qty')

admin.site.register(Product,ProductAdmin)




