from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView

from . import views

app_name = 'registration'
urlpatterns = [
    url('login/', auth_views.login, name='login'),
    url('logout/', views.user_logout, name='user_logout'),
    url('register/', views.register),
]