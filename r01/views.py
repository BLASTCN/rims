from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
from r01 import models
import time

class UserLoginForm(forms.Form):
    """登录表单验证"""
    user = forms.CharField(
        required=True,
        error_messages={'required': '用户名不能为空'}
    )
    pwd = forms.CharField(
        required=True,
        min_length=6,
        max_length=12,
        error_messages={'required': '密码不能为空', 'min_length': '密码长度不能小于6', 'max_length': '密码长度不能大于12'}
    )


def login(request):
    """用户登录"""
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        uname = request.POST.get('user')
        pwd = request.POST.get('pwd')
        ulf_obj = UserLoginForm(request.POST)
        # 先对提交的表单进行验证
        if ulf_obj.is_valid():
            # 再对用户名和密码进行验证
            obj = models.UserInfo.objects.filter(username=uname, password=pwd).first()
            if obj:
                # 设置session 并设置过期时间
                request.session['username'] = uname
                request.session['is_login'] = True
                request.session.set_expiry(60 * 60 * 24 * 3)
                return redirect('/r01/sensor')
            else:
                return render(request, 'login.html', {'err_message': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'ulf': ulf_obj})


def sensor_data(request):
    """登录后主页"""
    if request.session.get('is_login', None):
        return render(request, 'sensor/infrared-data.html', {'username': request.session['username']})
    else:
        return redirect('/r01/login')


def register_user(request):
    """用户注册 暂没开放"""
    if request.method == 'POST':
        format_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        uname = request.POST.get('user')
        pwd = request.POST.get('pwd')
        obj = models.UserInfo.objects.create(username=uname, password=pwd, regtime=format_time)
        if obj:
            pass
        pass
