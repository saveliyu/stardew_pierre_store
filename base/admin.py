from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image']
    list_filter = ['name']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}