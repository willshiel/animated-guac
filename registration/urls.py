from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from . import views

app_name = 'registration'
urlpatterns = [
    url('login/', auth_views.login, name='login'),
    url('logout/', auth_views.logout, name='logout'),
    url('register/', views.register)
]