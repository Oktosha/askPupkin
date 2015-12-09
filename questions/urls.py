from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'questions'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/', auth_views.login, name='login')
]