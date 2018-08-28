from django.conf.urls import url
import apps.product.views as product

app_name = 'products'

urlpatterns = [
    url(r'^$', product.index, name='index'),
    url(r'^(\d+)/$', product.index, name='index'),
    url(r'^(\d+)/(\d+)$', product.view, name='view'),
]