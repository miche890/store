from django.contrib import admin

from .models import Category, Product, Stock


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class StockInline(admin.TabularInline):
    model = Stock


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        StockInline
    ]
    list_display = ('name', 'description', 'category', 'price')
    search_fields = ('name', 'category__name', 'price')
    list_filter = ('category', 'price')


# Register your models here.
