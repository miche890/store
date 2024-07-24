from django.urls import path

from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.product_list, name='product_list'),
    path('productos/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('productos/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    # path('', views.index, name='index'),
    # path('store/category/list/', views.CategoryListView.as_view(), name='category_list'),
    # path('store/category/add/', views.CategoryAddView.as_view(), name='category_add'),
    # path('store/category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    # path('store/category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
]