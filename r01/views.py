from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django import forms
from r01 import models
import time
import json
from django.core import serializers

tab_names = [
    ['序号', '采集时间', '机器人号', '机器人位姿', '传感器01', '传感器02', '传感器03', '传感器04', '传感器05', '传感器06', '传感器07', '传感器08', '传感器09',
     '传感器11', '传感器12', '传感器13', '传感器14', '传感器15', '传感器16', '传感器17', '传感器18', '传感器19', '传感器20', '传感器21', '传感器22',
     '传感器23', '传感器24'],
    ['序号', '采集时间', '机器人号', '机器人位姿', '场景', '数据文件名', '数据文件路径', '区域01', '区域02', '区域03'],
    ['序号', '采集时间', '机器人号', '机器人位姿', '场景', '文件名', '图像路径'],
    ['序号', '采集时间', '机器人号', '机器人位姿', '场景', '深度数据文件名', '深度数据路径', '映射图像文件名', '映射图像路径']
]

m2t_dict = {
    'InfraredSensor': tab_names[0],
    'ultrasonicsensor': tab_names[0],
    'lasersensor': tab_names[1],
    'forwardvisionsensor': tab_names[2],
    'overallviewsensor': tab_names[2],
    'kinectvideosensor': tab_names[2],
    'kinectdeepsensor': tab_names[3]
}


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


def home(request):
    """主页"""
    pass


def sensor(request):
    """传感器页面"""
    return render(request, 'sensor.html')


def sensor_detail(request, sname):
    """传感器详情"""
    # 封装返回的json数据
    res = build_sensor_json(sname)
    return HttpResponse(res, content_type='application/json')


def build_sensor_json(sname):
    """生成json数据"""
    res = {'status': True, 'error': None, 'tabs': None, 'data': None}
    try:
        # 获取数据库中的数据
        objs = eval('models.' + sname + '.objects.all()')
        # object - (serialize) -> str - (json.loads) -> list
        serialize_data = serializers.serialize('json', objs)
        # type list
        json_data = json.loads(serialize_data)
        print(json_data)
        res['tabs'] = m2t_dict[sname]
        res['data'] = serializers.serialize('json', objs)
    except LookupError as e:
        res['status'] = False
        res['error'] = e.__str__()
    return json.dumps(res)


def fetch_data(tname):
    """返回相应的数据"""
    # TODO 如何将字符串表名称直接进行使用
    models.InfraredSensor.objects.all()
    return 'None'


def state(request):
    """机器人状态数据"""
    return render(request, 'state.html')


def envir(request):
    """工作环境信息"""
    return render(request, 'envir.html')


def data_result(request):
    """数据处理结果"""
    return render(request, 'result.html')


def tactic(request):
    """策略决策"""
    return render(request, 'tactic.html')


def register_user(request):
    """用户注册 暂不开放"""
    if request.method == 'POST':
        format_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        uname = request.POST.get('user')
        pwd = request.POST.get('pwd')
        obj = models.UserInfo.objects.create(username=uname, password=pwd, regtime=format_time)
        if obj:
            pass
        pass
