from django.contrib import admin
from django.urls import path
from django.conf.urls import url
import mainapp.views as mainapp

urlpatterns = [
    url(r'^$', mainapp.main),
    url(r'^products/', mainapp.products),
    url(r'^contact/', mainapp.contact),
    path('admin/', admin.site.urls),
]
