from django.conf.urls import url
import apps.order.views as order

app_name = 'order'

urlpatterns = [
    url(r'^$', order.view, name='view'),
    url(r'^add/(?P<pk>\d+)/$', order.add, name='add'),
    url(r'^remove/(?P<pk>\d+)/$', order.remove, name='remove'),
]

