from django.contrib import admin
from .models import Catalog
from .models import Cart
from .models import Checkout


# Register your models here.
admin.site.register(Catalog)
admin.site.register(Cart)
admin.site.register(Checkout)
