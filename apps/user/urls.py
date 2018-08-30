from django.conf.urls import url
import apps.user.views as user

app_name = 'user'

urlpatterns = [
    url(r'^login/$', user.login, name='login'),
    url(r'^logout/$', user.logout, name='logout'),
]
