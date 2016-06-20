from django.conf.urls import url, include
from django.contrib.auth.models import User
from assets_management.models import *
from user_management.models import *
from rest_framework import routers, serializers, viewsets
from django.shortcuts import render,redirect,RequestContext
from django.shortcuts import HttpResponse,render_to_response

def check_login_info(func):
    def wrapper(request,*args,**kwargs):
        if request.session.get('islogin'):
            return func(request,*args,**kwargs)
        else:
            return redirect('/404/')
    return wrapper

# Serializers define the API representation.
#################room
class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MachineRoom
        fields = ('macroom',)

# ViewSets define the view behavior.
class RoomViewSet(viewsets.ModelViewSet):
    queryset = MachineRoom.objects.all()
    serializer_class = RoomSerializer


#################cabinet
class CaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cabinet
        fields = ('cabinet','room')

# ViewSets define the view behavior.
class CaViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CaSerializer

#################machines
class MgmaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Machines
        fields = ('ip', 'role', 'hardwareinfo', 'gameinfo','cb','room')

# ViewSets define the view behavior.
class MgmaViewSet(viewsets.ModelViewSet):
    queryset = Machines.objects.all()
    serializer_class = MgmaSerializer

###############user_management
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = userinfo
        fields = ('username','password','is_active','privilege')

class UserViewSet(viewsets.ModelViewSet):
    queryset = userinfo.objects.all()
    serializer_class = UserSerializer