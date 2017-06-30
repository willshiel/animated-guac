from django.conf.urls import url

from . import views

app_name = 'picks'
urlpatterns = [
    url('picks/', views.picks_home, name='login'),
]