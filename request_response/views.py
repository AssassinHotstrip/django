import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def weather(request, city, year):
    # 演示正则组抽取URL中位置参数
    print(city)
    print(year)

    return HttpResponse('weather')



def weather2(request, year, city):
    # 演示正则组抽取URL中关键字参数
    print(city)
    print(year)

    return HttpResponse('weather2')

# http://127.0.0.1:8000/query_str/?a=10&b=20&a=30
def query_str(request):
    # 演示提取查询字符串数据
    # request.GET 返回一个QueryDict类的对象。类似字典
    a = request.GET.get('a')  # 一键一值，如果有多值会取最后一个值
    b = request.GET.get('b')
    a_list = request.GET.getlist('a')  # 一键多值，返回列表
    print(a)
    print(b)
    print(a_list)
    return HttpResponse('query_str')



def query_form(request):
    """演示提取请求体中的表单数据"""
    # request.POST 返回一个QueryDict 类的对象，类似字典
    like = request.POST.get('like')  # 一键一值，如果有多值会取最后一个值
    b = request.POST.get('b')
    like_list = request.POST.getlist('like')

    print(like)
    print(b)
    print(like_list)
    return HttpResponse('query_form')



def body_json(request):
    """演示提取请求体中的非表单数据  如json"""
    bytes_str = request.body  # 获取请求体中的非表单数据，字节类型
    json_str = bytes_str.decode()  #将二进制转换为字符串
    json_dict = json.loads(json_str)  # 将json格式的字符串转换成json格式的字典
    print(json_dict)

    return HttpResponse('body_json')



def request_head(request):
    """演示获取请求头信息"""
    con_type = request.META["CONTENT_TYPE"]
    print(con_type)

    print(request.method, request.path)
    return HttpResponse('request_head')



def response_demo(request):
    """演示响应操作"""
    # HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)

    return HttpResponse('response_demo',content_type='text/html', status=207)

    # , content_type = 'text/html', status = 204
    # response = HttpResponse('ok')
    # response['Itcast'] = 'Python'
    # return response

# GET//response_json/
def response_json(request):
    """演示响应json数据"""
    # json中的引号一定要用双引号
    json_dict = {"name": "Kakashi", "age": "18"}

    return JsonResponse(json_dict)

# GET//response_demo/
def reverse_demo(request):
    """演示路由的命名和反向解析"""

    # 正向解析：通过路由找视图
    # 反向解析：通过视图找路由（在url中给路由起别名））
    url = reverse('reverse_demo')
    print(url)
    return HttpResponse('request_response:reverse_demo')


# GET//redirect_demo/
def redirect_demo(response):
    """演示重定向"""

    # 重定向时，直接拼接新路径，会在当前路径下拼接新的路径
    # 若在新路径前加  / ， 则从根路径拼接
    # return redirect("/users/index")  #为防止被重定向的路由更改后引起不便，不建议这样写

    # 利用反向解析灵活重定向
    return redirect(reverse("users:reverse_demo"))


# GET//cookie_demo/
def cookie_demo(request):
    """cookie缓存数据读写"""
    # 设置cookie 需要通过响应对象设置
    response = HttpResponse("cookie_demo")
    #                    key      value    过期时间s
    response.set_cookie("name", "Kakashi", max_age=3600)

    # 读取cookie 需要通过请求对象
    name = request.COOKIES.get("name")
    print(name)
    return response


# GET//session_demo/
def session_demo(request):
    """演示session缓存读写"""
    # 设置session
    request.session["name"] = "Kakashi"
    # 存储session时，会自动生成一个session_id
    # 后面会把该session_id通过响应对象写入到浏览器的cookie中

    # 读取session
    name = request.session.get("name")
    # 通过request带过来的cookie取到session_id
    # 通过session_id 取出对应的session记录
    # 通过session的key取到值

    print(name)

    return HttpResponse("session_demo")