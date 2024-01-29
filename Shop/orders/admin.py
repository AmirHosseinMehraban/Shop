from django.contrib import admin
from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user']
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']
admin.site.register(OrderItem, OrderItemAdmin)

# Register your models here.
