from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Catalog
from .models import Cart
from .models import Checkout


# Register your models here.
class CatalogAdmin(admin.ModelAdmin):
    fields = ['ProductName', 'ProductMaker', 'ProductBrand', 'ProductPrice', 'ProductCategory', 'ProductFeatures',
              'ProductDescription', 'ProductImage', 'preview', 'ProductMetaTittle',
              'ProductMetaKeywords', 'ProductMetaDescription', 'ProductIsrail']
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.ProductImage.url}" height="197" width="197">')


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Cart)
admin.site.register(Checkout)
