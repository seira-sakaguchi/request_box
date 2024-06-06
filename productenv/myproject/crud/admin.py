from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'price', 'stock', 'purchase_code')
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
