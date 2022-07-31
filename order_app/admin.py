from django.contrib import admin
from .models import Order, Product
# Register your models here.


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'placed', 'total_price', 'total_qty']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'brand', 'name', 'price', 'qty']