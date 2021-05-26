from django.shortcuts import render
from django.views.generic import View
from .forms import CatalogForm
from .models import Catalog


# Create your views here.
def catalog_add_product(request):
    data = {}
    error = ''
    if request.method == "POST":
        form = CatalogForm(request.POST, request.FILES)
        if form.is_valid():
            pass
        else:
            error = "Login or Password was incorrect!"

    form = CatalogForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'catalog/catalog-add-product.html', data)


class ProductIndex(View):

    def catalog_index(request):
        return render(request, 'catalog/catalog_index.html')


class ProductCart(View):

    def catalog_cart(request):
        return render(request, 'catalog/catalog-cart.html')


class ProductCheckout(View):

    def catalog_checkout(request):
        return render(request, 'catalog/catalog-checkout.html')


class ProductCustomers(View):

    def catalog_customers(request):
        return render(request, 'catalog/catalog-customers.html')


class ProductOrders(View):

    def catalog_orders(request):
        return render(request, 'catalog/catalog-orders.html')


class ProductDetail(View):

    def catalog_product_detail(request):
        return render(request, 'catalog/catalog-product-detail.html')
