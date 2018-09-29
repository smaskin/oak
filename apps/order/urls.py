from django.conf.urls import re_path
import apps.order.views as order

app_name = 'order'

urlpatterns = [
    re_path(r'^$', order.index, name='index'),
    re_path(r'^cart/', order.cart, name='cart'),
    re_path(r'^view/', order.view, name='view'),
    re_path(r'^edit/(?P<pk>\d+)/(?P<quantity>\d+)/$', order.edit, name='edit'),
    re_path(r'^add/(?P<pk>\d+)/$', order.add, name='add'),
    re_path(r'^remove/(?P<pk>\d+)/$', order.remove, name='remove'),
    re_path(r'^pay$', order.pay, name='pay'),
]
