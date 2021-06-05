from django.shortcuts import render, redirect
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
    try:
        if request.session['user'] is not None:
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
    except KeyError:
        return redirect('http://127.0.0.1:8000/')


class ProductDetailView(DetailView):
    model = Catalog
    template_name = 'catalog/catalog-product-detail.html'
    context_object_name = 'detail'


class ProductIndex(View):

    def catalog_index(request):
        all_products = ''
        all_category = ''
        all_category_deep = ''
        pish = Cart.objects
        if request.method == "POST":
            p_id = request.POST['id']
            p_count = request.POST['count']
            user = request.session['user']
            time = timezone.now()

            if pish.filter(ProductIdSold__in=p_id).exists():
                old_count = pish.filter(ProductIdSold__in=p_id).values('ProductCountSold')
                for ccount in old_count:
                    ccount = ccount
                new_count = int(ccount['ProductCountSold']) + int(p_count)
                pish.filter(ProductIdSold__in=p_id).update(ProductCountSold=new_count)
            else:
                pish.create(ProductIdSold=p_id, ProductCountSold=p_count, UserNameSold=user, SoldTime=time)
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
        pr = self.request.GET.getlist("price")
        pr = pr[0].split(';')
        price_var = range(int(pr[0]), int(pr[1]))
        if self.request.GET.getlist("category") and price_var is not None:
            queryset = Catalog.objects.filter(
                Q(ProductFeatures__in=self.request.GET.getlist("category")) &
                Q(ProductPrice__in=price_var)
            ).distinct().values('ProductId', 'ProductImage', 'ProductFeatures', 'ProductName', 'ProductPrice')
            return queryset
        elif self.request.GET.getlist("category"):
            queryset = Catalog.objects.filter(
                Q(ProductFeatures__in=self.request.GET.getlist("category"))
            ).distinct().values('ProductId', 'ProductImage', 'ProductFeatures', 'ProductName', 'ProductPrice')
            return queryset
        elif price_var is not None:
            queryset = Catalog.objects.filter(
                Q(ProductPrice__in=price_var)
            ).distinct().values('ProductId', 'ProductImage', 'ProductFeatures', 'ProductName', 'ProductPrice')
            return queryset


    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"filtered": queryset}, safe=False)


class ProductCart(View):

    def catalog_cart(request):

        cart = Cart.objects
        cat = Catalog.objects
        jopa = cart.values('ProductIdSold')
        if not jopa:
            return render(request, 'catalog/catalog-cart.html')
        else:
            x = 0
            i = 0
            almost_final = 0
            final_price = []
            new_price = []
            last_count = 0
            qs = Q()

            counter = cart.values('ProductIdSold', 'ProductCountSold')

            sorted_tuples = sorted(counter, key=operator.itemgetter('ProductIdSold'))

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

            if request.method == "POST":
                cart.filter(ProductIdSold__in=ProductId).delete()
                return redirect('/catalog/cart')

            data = {
                'p_price': final_price,
                'count': sorted_tuples,
                'fincat': fincat,
                'final_price': almost_final,
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
