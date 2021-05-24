from django.contrib import admin
from .models import Catalog
from .models import Cart


# Register your models here.
admin.site.register(Catalog)
admin.site.register(Cart)
