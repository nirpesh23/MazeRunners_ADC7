from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',view_register_user),
    path('restrictpage/',view_hello_world),
    path('accounts/login/',view_authenticate_user),
    path('printhello/',hello),
]