from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'registration'
urlpatterns = [
    url('^$', auth_views.login, name='login'),
]