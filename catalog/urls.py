from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_index, name='catalog.index'),
    path('product-detail', views.catalog_product_detail, name='catalog.detail'),
    path('cart', views.catalog_cart, name='catalog.cart'),
    path('checkout', views.catalog_checkout, name='catalog.checkout'),
    path('customers', views.catalog_customers, name='catalog.customers'),
    path('orders', views.catalog_orders, name='catalog.orders'),
    path('add-product', views.catalog_add_product, name='catalog.add_product'),
]