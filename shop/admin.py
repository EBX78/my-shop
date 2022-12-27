from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'in_stock', 'is_active', 'fcreated', 'fupdated', 'category']
    search_fields = ['title', 'slug', 'category']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['in_stock', 'is_active', 'price']
    prepopulated_fields = {'slug':('title',)}
    ordering = ['id']