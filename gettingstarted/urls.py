from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^registration/', include('registration.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^picks/', include('picks.urls')),
    url(r'^$', RedirectView.as_view(url='/registration/login', permanent=True)),
]