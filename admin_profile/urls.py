from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_profile_index, name='admin_profile.index'),
]