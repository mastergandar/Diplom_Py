from django.urls import path
from . import views

urlpatterns = [
    path('', views.rab_profile_index, name='rab_profile.index'),
]