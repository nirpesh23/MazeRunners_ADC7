
from django.contrib import admin
from django.urls import path,include
from products.views import view_authenticate_user

from products.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include('profile_maker.urls')),
]


urlpatterns += [
    path('products/',include('products.urls'))
]
urlpatterns += [
    path('restapi/',include('restapi.urls'))
]

urlpatterns += [
    # path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/login/',view_authenticate_user)
]
urlpatterns += [
    path('products/',include('products.urls')),
    path('restapi/',include ('restapi.urls'))
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
