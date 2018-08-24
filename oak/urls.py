from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

import mainapp.views as mainapp
import productapp.views as productapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('contact', mainapp.contact, name='contact'),
    path('products', include(('productapp.urls', 'index'), namespace='products')),
    path('detail', productapp.view, name='detail'),
    path('admin', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
