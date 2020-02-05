from django.urls import path
from .views import view_get_post_products
from .views import view_getByID_updateByID_deleteByID


urlpatterns = [
    path('Product1/',view_get_post_products),
    path('Product2/<int:ID>',view_getByID_updateByID_deleteByID),
]