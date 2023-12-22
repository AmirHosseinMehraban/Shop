from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_available']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
