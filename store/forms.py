from django import forms

from .models import Category, Product, Stock


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price']


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'quantity']
