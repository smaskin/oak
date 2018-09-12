from django.conf.urls import re_path
import apps.user.views as user

app_name = 'user'

urlpatterns = [
    re_path(r'^login/$', user.login, name='login'),
    re_path(r'^logout/$', user.logout, name='logout'),
    re_path(r'^register/$', user.register, name='register'),
    re_path(r'^edit/$', user.edit, name='edit'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', user.verify, name='verify')
]