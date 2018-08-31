from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

import apps.main.views as main

urlpatterns = [
    path('product/', include('apps.product.urls', namespace='product')),
    path('user/', include('apps.user.urls', namespace='user')),
    path('order/', include('apps.order.urls', namespace='order')),
    path('admin/', admin.site.urls),
    path('', main.main, name='main')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
