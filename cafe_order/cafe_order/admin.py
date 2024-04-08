from django.contrib import admin
from cafe_order.models import Item, Order, Category 

@admin.register(Item)  
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')

@admin.register(Order)  
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'order_date', 'item_count', 'order_price')

@admin.register(Category) 
class CafeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
