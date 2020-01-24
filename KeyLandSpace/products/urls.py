from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('productpage',view_product_page),
    path('productlist/',view_product_details),
    path('productform/',view_product_form),
    path('productform/save',view_productlist_save),
    path('productsearch/',view_search_item),
]