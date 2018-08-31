from django.conf.urls import url
import apps.product.views as product

app_name = 'product'

urlpatterns = [
    url(r'^$', product.index, name='index'),
    url(r'^(?P<category>\d+)$', product.index, name='index'),
    url(r'^(\d+)/(\d+)$', product.view, name='view'),
]