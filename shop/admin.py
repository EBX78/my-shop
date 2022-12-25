from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'fprice', 'in_stock', 'is_active', 'fcreated', 'fupdated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['in_stock', 'is_active']
    prepopulated_fields = {'slug':('title',)}
