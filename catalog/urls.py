from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_index, name='catalog.index'),
]