#!/usr/bin/evn python
#coding:utf8
from django.shortcuts import render
from django.shortcuts import render,redirect,RequestContext
from django.shortcuts import HttpResponse,render_to_response,redirect
import models
import json
import commands
import subprocess
import linecache
import json
import commands
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie

#session判断用户是否登录和有操作权限装饰器函数
def check_login_option_privilege(func):
    def wrapper(request,*args,**kwargs):
        if request.session.get('islogin'):
            if str(3) in str(request.session.get('privilege')):
                return func(request,*args,**kwargs)
            elif str(1) in str(request.session.get('privilege')):
                return redirect('/user/info/1/',context_instance=RequestContext(request))
            elif str(2) in str(request.session.get('privilege')):
                return redirect('/assets/mgroom/1/',context_instance=RequestContext(request))
            else:
                return redirect('/404/',context_instance=RequestContext(request))
        else:
            return redirect('/login/',context_instance=RequestContext(request))
    return wrapper

# Create your views here.
@check_login_option_privilege
def install_server(request):
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
    return render_to_response('install.html',info,context_instance=RequestContext(request))

@check_login_option_privilege
def update_server(request):
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
    return render_to_response('update.html',info,context_instance=RequestContext(request))

@check_login_option_privilege
def open_server(request):
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
    return render_to_response('open.html',info,context_instance=RequestContext(request))

@check_login_option_privilege
def close_server(request):
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
    return render_to_response('close.html',info,context_instance=RequestContext(request))


@check_login_option_privilege
def remoteoptions(request):
    if request.method == 'POST' and request.is_ajax():
        #data = request.POST
        #for key in data:
            #info = eval(key)
            #print key
        info = json.loads(request.body)
        if info['option'] == 'install'and info['ser_id'] != "None" and info['svn_v'] != "None" and info['names'] != "None" and info['mess'] != "None":
            print info['ser_id'],info['svn_v'],info['names'],info['mess']
            output = subprocess.Popen('python d:\py_work\install.py',shell=True,stderr=subprocess.STDOUT,stdout=subprocess.PIPE)
            return HttpResponse('OK')
        elif info['option'] == 'update' and info['ser_id'] != "None" and info['svn_v'] != "None":
            print info['ser_id'],info['svn_v']
            output = subprocess.Popen('python d:\py_work\install.py',shell=True,stderr=subprocess.STDOUT,stdout=subprocess.PIPE)
            return HttpResponse('OK')
        elif info['option'] == 'open' and info['ser_id'] != "None" and info['mess'] != "None" and info['stat'] != "None":
            print info['ser_id'],info['mess'],info['stat']
            output = subprocess.Popen('python d:\py_work\install.py',shell=True,stderr=subprocess.STDOUT,stdout=subprocess.PIPE)
            return HttpResponse('OK')
        elif info['option'] == 'close' and info['ser_id'] != "None" and info['mess'] != "None":
            print info['ser_id'],info['mess']
            output = subprocess.Popen('python d:\py_work\install.py',shell=True,stderr=subprocess.STDOUT,stdout=subprocess.PIPE)
            return HttpResponse('OK')
        else:
            #清空日志
            file = open('d:\py_work\\test.txt','w')
            file.close()
            info = json.dumps({'status':'error'})
            return HttpResponse(info,context_instance=RequestContext(request))
            #for i in output.stdout.readlines():
            #    print i,


@check_login_option_privilege
def readoutput(request):
    if request.method == "POST" and request.is_ajax():
        data = json.loads(request.body)
        start = int(data['line'])
        end = len(open(r'D:\py_work\test.txt','rU').readlines())
        #print start,end
        with open('d:\py_work\\test.txt') as file:
            data01 = file.readlines()[start:end]
        #print data01
        content = ' '.join(data01)
        datainfo = json.dumps({'lines':end,'content':content})
        #print datainfo
        #print datainfo
        return HttpResponse(datainfo)
