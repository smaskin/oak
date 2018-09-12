from django.conf.urls import re_path
import apps.product.views as product

app_name = 'product'

urlpatterns = [
    re_path(r'^$', product.index, name='index'),
    re_path(r'^(?P<category>\d+)$', product.index, name='index'),
    re_path(r'^(\d+)/(\d+)$', product.view, name='view'),
]