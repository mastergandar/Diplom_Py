from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.ProductIndex.catalog_index, name='catalog.index'),
    path('json-filter/', views.JsonFilterCatalogView.as_view(), name='json_filter'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='catalog.detail'),
    path('cart', views.ProductCart.catalog_cart, name='catalog.cart'),
    path('checkout', views.ProductCheckout.catalog_checkout, name='catalog.checkout'),
    path('delete', views.ProductDelete.catalog_delete, name='catalog.delete'),
    path('orders', views.ProductOrders.catalog_orders, name='catalog.orders'),
    path('add-product', views.catalog_add_product, name='catalog.add_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)