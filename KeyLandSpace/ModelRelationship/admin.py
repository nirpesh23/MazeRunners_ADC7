from django.contrib import admin
from .models import Buyer,Seller,Customer,Product,Order_items,Order


# Register your models here.
admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order_items)
admin.site.register(Order)
