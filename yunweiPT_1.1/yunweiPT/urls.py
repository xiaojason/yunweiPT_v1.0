"""yunweiPT URL Configuration

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
from django.conf.urls import url,include,patterns
from django.contrib import admin
from assets_management.views import *
import assets_management.urls
import user_management.urls
import options.urls
import api.urls
import settings
from user_management.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^assets/', include('assets_management.urls')),
    url(r'^user/',include('user_management.urls')),
    url(r'^options/',include('options.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^login/',login),
    url(r'^changepassword/',changepassword),
    url(r'^404/',pager_not_found),
]
