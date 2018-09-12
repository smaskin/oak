from django.conf.urls import re_path
import apps.order.views as order

app_name = 'order'

urlpatterns = [
    re_path(r'^$', order.view, name='view'),
    re_path(r'^add/(?P<pk>\d+)/$', order.add, name='add'),
    re_path(r'^remove/(?P<pk>\d+)/$', order.remove, name='remove'),
]

