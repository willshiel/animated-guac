from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^matchup', views.matchup, name='matchup')
]