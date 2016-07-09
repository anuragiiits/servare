"""boar_bar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from share.views import home_view


urlpatterns = [
    url(r'^$', home_view, name='home_view'),
    url(r'^user/', include('user.urls')),
    url(r'^admin/?', admin.site.urls),
    url(
        r'^dict/?',
        include('dictionary.urls')
    ),
    url(
        r'^discussion/?',
        include('discussion.urls')
    ),
    url(
        r'^collection/?',
        include('collection.urls')
    ),
    url(
        r'^favicon\.ico$',
        RedirectView.as_view(url='/static/favicon.png', permanent=True)
    ),
    #url(
    #    r'^.*$',
    #    RedirectView.as_view(
    #        url='dict',
    #        permanent=False
    #    ),
    #    name='index'
    #),
]

if settings.DEBUG:
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
