from django.conf.urls import url
import productapp.views as productapp

urlpatterns = [
    url(r'^$', productapp.index, name='index'),
    url(r'^(\d+)/$', productapp.view, name='view'),
]
