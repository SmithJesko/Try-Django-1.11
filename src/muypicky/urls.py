from django.conf.urls import url
from django.contrib import admin

from restaurants.views import home, about, contact

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^about/$', about),
    url(r'^contact/$', contact),
]
