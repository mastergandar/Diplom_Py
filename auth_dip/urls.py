from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_dip_index, name='auth.index'),
]