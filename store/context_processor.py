from store.models import Category


def store_context(request):
    categories = Category.objects.all()
    categories_highlight = Category.objects.filter(highlight=True)
    return {
        'categories': categories,
        'categories_highlight': categories_highlight
    }
