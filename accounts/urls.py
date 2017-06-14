from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'profile/(?P<user_id>[0-9]+)/$', views.profile),
]