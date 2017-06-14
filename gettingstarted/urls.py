from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('registration.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^home/', include('home.urls')),
]
