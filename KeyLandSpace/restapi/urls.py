from django.urls import path
from .views import view_get_post_products
from .views import view_getByID_updateByID_deleteByID


urlpatterns = [
    path('products/',view_get_post_products),
    path('products/<int:ID>',view_getByID_updateByID_deleteByID),
]