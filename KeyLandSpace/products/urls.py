from django.contrib import admin
from django.urls import path,include
from django.urls import path
from .views import *

urlpatterns = [
    path('productpage',view_product_page),
    path('productlist/',view_product_details),
    path('productform/',view_product_form),
    path('productform/save',view_productlist_save),
    path('productsearch/',search),



     path('productlist/edit/<int:ID>',view_productdata_updateform),
     path('productlist/edit/update/<int:ID>',view_update_form_data_in_db),
     path('productlist/',view_product_details),
     path('homepage/', view_homepage),
     path('signup/',view_register_user),		
     path('aboutus/', view_aboutus),
     path('signup/',view_register_user),	
	 

    path('restrictpage/',view_hello_world),
    path('accounts/login/',view_authenticate_user),
    path('printhello/',hello),
    
from django.urls import path
from .views import *

urlpatterns = [
    path('productpage',view_product_page),
    path('productlist/',view_product_details),
    path('productform/',view_product_form),
    path('productform/save',view_productlist_save),
    path('productsearch/',search),
    
]