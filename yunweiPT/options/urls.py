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
from django.conf.urls import url
from options.views import *

urlpatterns = [
    url(r'install/',install_server),
    url(r'remoteoptions/',remoteoptions),
    url(r'readoutput/',readoutput),
    url(r'update/',update_server),
    url(r'open/',open_server),
    url(r'close/',close_server),
    #url(r'update/',update_server),
    #url(r'open_and_close/',open_server),
]