from django.conf.urls import url

from . import views

app_name = 'profiles'
urlpatterns = [
    url(r'^profiles/\d+', views.get_profile),
]