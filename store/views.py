from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product, Stock


# Create your views here.
def index(request):
    return render(request, 'index.html')


def product_list(request, category_slug=None):
    # Category
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Order
    ordering = request.GET.get('order')
    if ordering:
        products = products.order_by(ordering)

    # Search
    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search)

    # Paginar productos
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'store/products/list.html',
        {
            'category': category,
            'categories': categories,
            'products': products,
            'page_obj': page_obj,
        }
    )


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm
    return render(
        request,
        'store/products/detail.html',
        {
            'product': product,
            'cart_product_form': cart_product_form,
        }
    )
