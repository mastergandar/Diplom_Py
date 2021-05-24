from django.shortcuts import render


# Create your views here.


def catalog_index(request):
    return render(request, 'catalog/catalog_index.html')


def catalog_add_product(request):
    return render(request, 'catalog/catalog-add-product.html')


def catalog_cart(request):
    return render(request, 'catalog/catalog-cart.html')


def catalog_checkout(request):
    return render(request, 'catalog/catalog-checkout.html')


def catalog_customers(request):
    return render(request, 'catalog/catalog-customers.html')


def catalog_orders(request):
    return render(request, 'catalog/catalog-orders.html')


def catalog_product_detail(request):
    return render(request, 'catalog/catalog-product-detail.html')
