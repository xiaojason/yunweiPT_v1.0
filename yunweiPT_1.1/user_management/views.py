#!/usr/bin/env python
#coding:utf8
from django.shortcuts import render,redirect,RequestContext
from django.shortcuts import HttpResponse,render_to_response
import models
from extension import assetsglobal
from random import sample
import json
import hashlib
import forms
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie

#session判断用户是否登录
def check_login_info(func):
    def wrapper(request,*args,**kwargs):
        if request.session.get('islogin'):
            return func(request,*args,**kwargs)
        else:
            return redirect('/login/',context_instance=RequestContext(request))
    return wrapper

def check_login(func):
    def wrapper(request,*args,**kwargs):
        if request.session.get('islogin'):
            if str(1) in str(request.session.get('privilege')):
                return func(request,*args,**kwargs)
            else:
                return redirect('/assets/mgroom/1/',context_instance=RequestContext(request))
        else:
            return redirect('/login/',context_instance=RequestContext(request))
    return wrapper
# Create your views here.
@check_login
def userinfo(request,page):
    page = assetsglobal.Init(page)
    totalitems = models.userinfo.objects.filter(id__gt=0).count()
    ROW = 5
    getitems = assetsglobal.getitems(int(page),int(totalitems),ROW)
    getitems01 = models.userinfo.objects.filter(id__gt=0)[getitems.From():getitems.To()]
    Totalpage = getitems.totalpage()
    getMark = assetsglobal.getmark('/user/info/',Totalpage,int(page))
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
    #print endinfo
    return render_to_response('user.html',endinfo,context_instance=RequestContext(request))

#密码加密
@check_login
def encrypwd(request):
    if request.method == 'POST' and request.is_ajax():
        data = json.loads(request.body)
        password = data['password']
        str = ''.join(sample('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789', 8))
        data01 = password + str
        encry = hashlib.md5(data01).hexdigest()
        data02 = encry + '@' + str
        data02 = json.dumps({'encryptionpwd':data02})
        return HttpResponse(data02)

#检查密码是否修改
@check_login
def checkpassword(request):
    if request.method == "POST" and request.is_ajax():
        data = json.loads(request.body)
        password = data['password']
        password = password.encode("utf-8")
        try:
            info = password.split('@')[1]
        except Exception,e:
            info = ""
        #print type(password)
        #print password,info
        if len(info) == 8:
            newdata = json.dumps({'encryptionpwd':password})
            return HttpResponse(newdata)
        else:
            str = ''.join(sample('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789', 8))
            data01 = password + str
            encry = hashlib.md5(data01).hexdigest()
            data02 = encry + '@' + str
            data02 = json.dumps({'encryptionpwd':data02})
            return HttpResponse(data02)

def login(request):
    if request.method == 'POST':
        form = forms.AuthModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = data['username']
            passwd = data['password']
            try:
                realpasswd = models.userinfo.objects.get(username=user).password
            except Exception,e:
                realpasswd = "@"
            realpasswd = realpasswd.encode('utf-8')
            salt = realpasswd.split('@')[1]
            userpassword = hashlib.md5(passwd + salt).hexdigest()
            userpassword = userpassword + "@" + salt
            rest = models.userinfo.objects.filter(username=user,password=userpassword)
            if rest:
                active = models.userinfo.objects.filter(username=user,password=userpassword).values('is_active')[0]['is_active']
                privilege = models.userinfo.objects.filter(username=user,password=userpassword).values('privilege')[0]['privilege']
                if active:
                    #print request.session[session_key]
                    request.session['islogin'] = True
                    request.session['user'] = user
                    request.session['privilege'] = privilege
                    if str(2) in str(privilege.encode('utf8')):
                        return redirect('/assets/mgroom/1/',context_instance=RequestContext(request))
                    elif str(1) in str(privilege.encode('utf8')):
                        return redirect('/user/info/1/',context_instance=RequestContext(request))
                    elif str(3) in str(privilege.encode('utf8')):
                        return redirect('/options/install/',context_instance=RequestContext(request))
                    else:
                        return redirect('/404/',context_instance=RequestContext(request))
                else:
                    print "unactive"
                    dic = {'inactive':True}
                    info = dict({'model':form},**dic)
                    return render_to_response('login.html',info,context_instance=RequestContext(request))
            else:
                dic = {'invailduspd':True}
                info = dict({'model':form},**dic)
                return render_to_response('login.html',info,context_instance=RequestContext(request))
        else:
            print form.errors
            return render_to_response('login.html',{'model':form},context_instance=RequestContext(request))
    #已经登录用户不会再看到登录页
    elif request.session.get('islogin'):
        privilege = request.session['privilege']
        if str(2) in str(privilege.encode('utf8')):
            return redirect('/assets/mgroom/1/',context_instance=RequestContext(request))
        elif str(1) in str(privilege.encode('utf8')):
            return redirect('/user/info/1/',context_instance=RequestContext(request))
        elif str(3) in str(privilege.encode('utf8')):
            return redirect('/options/install/',context_instance=RequestContext(request))
        else:
            return redirect('/404/',context_instance=RequestContext(request))
    else:
        form = forms.AuthModelForm()
        return render_to_response('login.html',{'model':form},context_instance=RequestContext(request))

def pager_not_found(request):
    return render_to_response('404.html')

@check_login_info
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('/login/',context_instance=RequestContext(request))