from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    """
    演示路由的匹配
    :param request: 视图最少要有一个参数，并且放在第一位接收请求对象（HttpRequest类型对象），内部包含请求报文信息
    :return: 响应对象（HttpResponse类型对象）内部包含响应报文信息
    """

    return HttpResponse("Helle django")



def say(request):
    return HttpResponse('say')


def say_hello(request):
    return HttpResponse('say hello')