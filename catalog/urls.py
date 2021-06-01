from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductIndex.catalog_index, name='catalog.index'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='catalog.detail'),
    path('cart', views.ProductCart.catalog_cart, name='catalog.cart'),
    path('checkout', views.ProductCheckout.catalog_checkout, name='catalog.checkout'),
    path('customers', views.ProductCustomers.catalog_customers, name='catalog.customers'),
    path('orders', views.ProductOrders.catalog_orders, name='catalog.orders'),
    path('add-product', views.catalog_add_product, name='catalog.add_product'),
]