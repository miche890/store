from django.contrib import admin

from .models import Category, Product, Stock


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'highlight']
    # list_editable = ['highlight']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


class StockInline(admin.TabularInline):
    model = Stock


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        StockInline
    ]
    list_display = ['name', 'slug', 'price', 'created', 'updated']
    list_filter = ['category', 'price', 'created', 'updated']
    list_editable = ['price']
    search_fields = ['name', 'category__name', 'price']
    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
