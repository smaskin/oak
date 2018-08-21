from django.contrib import admin
from django.urls import path
from django.conf.urls import url
import mainapp.views as mainapp

urlpatterns = [
    url(r'^$', mainapp.main, name='main'),
    url(r'^products', mainapp.products, name='products'),
    url(r'^contact', mainapp.contact, name='contact'),
    url(r'^detail', mainapp.detail, name='detail'),
    path('admin', admin.site.urls),
]
