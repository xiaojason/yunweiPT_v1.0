#coding:utf8
from django.conf.urls import url,include,patterns
from rest_framework import routers
from extend.apiview import *

#api接口
router = routers.DefaultRouter()
router.register(r'mgma',MgmaViewSet)
router.register(r'mgroom',RoomViewSet)
router.register(r'mgcb',CaViewSet)
router.register(r'user',UserViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
