from django.conf.urls import url

from home.views import List
from home.views import Home
from . import views

urlpatterns = [
    url(r'^list/$', List.as_view(), name='user_list'),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^new/$', views.user_new, name='user_new'),
]
