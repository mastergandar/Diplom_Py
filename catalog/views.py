from django.shortcuts import render
from django.views.generic import View, DetailView
from django.http import HttpResponse
from .forms import CatalogForm
from .models import Catalog
from django.core.files.storage import FileSystemStorage


# Create your views here.
class Custom():
    class Media:
        js = ('js/dropzone.min.js',)


def catalog_add_product(request):
    data = {}
    error = ''

    if request.method == "POST":
        form = CatalogForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        else:
            HttpResponse("Form is invalid!!!")

        # form.save()
    else:
        form = CatalogForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'catalog/catalog-add-product.html', data)


class ProductDetailView(DetailView):
    model = Catalog
    template_name = 'catalog/catalog-product-detail.html'
    context_object_name = 'detail'


class ProductIndex(View):

    def catalog_index(request):
        all_products = Catalog.objects.all()
        all_category = Catalog.CATEGORY
        all_category_deep = Catalog.CATEGORY_DEEP
        data = {
            'products': all_products,
        }
        return render(request, 'catalog/catalog_index.html', {'all_products': all_products,
                                                              'all_category': all_category,
                                                              'all_category_deep': all_category_deep})


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
