#coding:utf8
from django.shortcuts import render
from django.shortcuts import HttpResponse,render_to_response,redirect
from django.shortcuts import render,redirect,RequestContext
import models
from extension import assetsglobal


# Create your views here.
#判断用户是否已经登录并有资产管理权限装饰器
def check_login_privilege_assets(func):
    def wrapper(request,*args,**kwargs):
        if request.session.get('islogin'):
            if str(2) in str(request.session.get('privilege')):
                return func(request,*args,**kwargs)
            elif str(1) in str(request.session.get('privilege')):
                return redirect('/user/info/1')
            elif str(3) in str(request.session.get('privilege')):
                return redirect('/options/install')
            else:
                return redirect('/404/')
        else:
            return redirect('/login/')
    return wrapper

@check_login_privilege_assets
def mgroom(request,page):
    page = assetsglobal.Init(page)
    totalitems = models.MachineRoom.objects.filter(id__gt=0).count()
    ROW = 5
    getitems = assetsglobal.getitems(int(page),int(totalitems),ROW)
    getitems01 = models.MachineRoom.objects.filter(id__gt=0)[getitems.From():getitems.To()]
    Totalpage = getitems.totalpage()
    getMark = assetsglobal.getmark('/assets/mgroom/',Totalpage,int(page))
    #用户与权限
    user = request.session.get('user')
    privilege = request.session.get('privilege')
    info = {}
    pris = ['','user_mg_1','assets_mg_2','options_3']
    for i in xrange(1,4):
        if str(i) in privilege:
            info[pris[i]] = True
        else:
            info[pris[i]] = False
    info['user'] = user
    form = {}
    form['result'] = getitems01
    form['pager'] = getMark
    endinfo = dict({'model':form},**info)
    return render_to_response('mgassets.html',endinfo,context_instance=RequestContext(request))

@check_login_privilege_assets
def mgcb(request,page):
    page = assetsglobal.Init(page)
    totalitems = models.Cabinet.objects.filter(id__gt=0).count()
    ROW = 5
    getitems = assetsglobal.getitems(int(page),int(totalitems),ROW)
    getitems01 = models.Cabinet.objects.filter(id__gt=0)[getitems.From():getitems.To()]
    Totalpage = getitems.totalpage()
    getMark = assetsglobal.getmark('/assets/mgcb/',Totalpage,int(page))
    macroom = models.MachineRoom.objects.filter(id__gt=0)
    #用户与权限
    user = request.session.get('user')
    privilege = request.session.get('privilege')
    info = {}
    pris = ['','user_mg_1','assets_mg_2','options_3']
    for i in xrange(1,4):
        if str(i) in privilege:
            info[pris[i]] = True
        else:
            info[pris[i]] = False
    info['user'] = user
    form = {}
    form['result'] = getitems01
    form['pager'] = getMark
    form['macroom'] = macroom
    endinfo = dict({'model':form},**info)

    return render_to_response('mgcb.html',endinfo,context_instance=RequestContext(request))

@check_login_privilege_assets
def mgma(request,page):
    page = assetsglobal.Init(page)
    totalitems = models.Machines.objects.filter(id__gt=0).count()
    ROW = 5
    getitems = assetsglobal.getitems(int(page),int(totalitems),ROW)
    getitems01 = models.Machines.objects.filter(id__gt=0)[getitems.From():getitems.To()]
    Totalpage = getitems.totalpage()
    getMark = assetsglobal.getmark('/assets/mgma/',Totalpage,int(page))
    macroom = models.MachineRoom.objects.filter(id__gt=0)
    cbandroom = {}
    for i in macroom:
        cbs = models.Cabinet.objects.filter(room=i)
        cbandroom[i] = cbs

    #用户与权限
    user = request.session.get('user')
    privilege = request.session.get('privilege')
    info = {}
    pris = ['','user_mg_1','assets_mg_2','options_3']
    for i in xrange(1,4):
        if str(i) in privilege:
            info[pris[i]] = True
        else:
            info[pris[i]] = False
    info['user'] = user
    form = {}
    form['result'] = getitems01
    form['pager'] = getMark
    form['macroom'] = macroom
    form['cabinet'] = cbandroom
    endinfo = dict({'model':form},**info)
    return render_to_response('mgma.html',endinfo,context_instance=RequestContext(request))
