from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .models import Category, Product, Stock
from .forms import CategoryForm, ProductForm, StockForm


# Create your views here.

class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'store/categories/category_list.html'
    permission_required = 'store.view_category'


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'store/categories/category_detail.html'
    permission_required = 'store.view_category'


class CategoryAddView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'store/categories/category_add.html'
    permission_required = 'store.add_category'


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'store/categories/category_update.html'
    permission_required = 'store.change_category'
