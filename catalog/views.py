from django.shortcuts import render
from django.utils import timezone
from django.views.generic import View, DetailView, ListView
from django.http import HttpResponse, JsonResponse
from .forms import CatalogForm
from .models import Catalog, Cart
from django.db.models import Q
import operator
from django_filters.views import FilterView
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
        all_products = ''
        all_category = ''
        all_category_deep = ''
        if request.method == "POST":
            p_id = request.POST['id']
            p_count = request.POST['count']
            user = request.session['user']
            time = timezone.now()

            Cart.objects.create(ProductIdSold=p_id, ProductCountSold=p_count, UserNameSold=user, SoldTime=time)
            all_products = Catalog.objects.all()
            all_category = Catalog.CATEGORY
            all_category_deep = Catalog.CATEGORY_DEEP
            data = {
                'products': all_products,
            }
        else:
            all_products = Catalog.objects.all()
            all_category = Catalog.CATEGORY
            all_category_deep = Catalog.CATEGORY_DEEP
            data = {
                'products': all_products,
            }
        return render(request, 'catalog/catalog_index.html', {'all_products': all_products,
                                                              'all_category': all_category,
                                                              'all_category_deep': all_category_deep})


class JsonFilterCatalogView(ListView):
    def get_queryset(self):
        queryset = Catalog.objects.filter(
            Q(ProductFeatures__in=self.request.GET.getlist("category")) |
            Q(ProductPrice__in=self.request.GET.getlist("price"))
        ).distinct().values('ProductId', 'ProductImage', 'ProductFeatures', 'ProductName', 'ProductPrice')
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"filtered": queryset}, safe=False)



class ProductCart(View):

    def catalog_cart(request):
        cart = Cart.objects
        cat = Catalog.objects

        x = 0
        y = 0
        i = 0
        almost_final = 0
        final_price = []
        new_price = []
        last_count = 0
        qs = Q()

        counter = cart.values('ProductIdSold', 'ProductCountSold')

        sorted_tuples = sorted(counter, key=operator.itemgetter('ProductIdSold'))

        """for f in sorted_tuples:
            for key in f:
                f_arg = int(f[key[0]])
                s_arg = int(f[key[1]])
                final_price = f_arg * s_arg"""

        allid = cart.values_list('ProductIdSold')
        new_allid = list(set(allid))

        for ProductId in new_allid:
            qs = qs | Q(ProductId__in=ProductId)
        fincat = cat.filter(qs)

        for cat in fincat:
            cat = cat
            new_price.append(int(getattr(cat, 'ProductPrice')))

        while i < len(sorted_tuples):
            final_price.append(int(sorted_tuples[i]['ProductCountSold']) * new_price[i])
            i += 1

        while x < len(final_price):
            almost_final += final_price[x]
            x += 1

        """for product in counter:
            last_count = product
        for i in fincat:
            for c in sorted_tuples:
                if int() is i.values_list('ProductId', flat=True):
                    new_price = c.values_list('ProductCountSold') * i.values_list('ProductPrice')"""
        """for i in fincat:
            for c in sorted_tuples:
                if int(c['ProductIdSold']) is i['ProductId']:
                    new_price = c['ProductCountSold'] * i['ProductPrice']"""

        data = {
            'p_price': final_price,
            'count': sorted_tuples,
            'fincat': fincat,
            'final_price': almost_final,
            'y': y,
        }

        return render(request, 'catalog/catalog-cart.html', data)


class ProductCheckout(View):

    def catalog_checkout(request):
        return render(request, 'catalog/catalog-checkout.html')


class ProductCustomers(View):

    def catalog_customers(request):
        return render(request, 'catalog/catalog-customers.html')


class ProductOrders(View):

    def catalog_orders(request):
        return render(request, 'catalog/catalog-orders.html')
