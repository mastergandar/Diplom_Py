from django.shortcuts import render


# Create your views here.


def catalog_index(request):
    return render(request, 'catalog/catalog_index.html')
