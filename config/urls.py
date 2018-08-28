from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

import apps.main.views as main
import apps.product.views as product

urlpatterns = [path('contact', main.contact, name='contact'),
    path('products/', include('apps.product.urls', namespace='products')), path('admin', admin.site.urls),
    path('', main.main, name='main')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
