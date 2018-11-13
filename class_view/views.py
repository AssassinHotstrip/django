from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
# Create your views here.


def my_decorator(view_func):
    """装饰器"""

    def wrapper(request, *args, **kwargs):
        print("装饰器被调用")
        return view_func(request, *args, **kwargs)

    return wrapper

# 装饰函数演示
# @my_decorator
# def test(request):
#     return HttpResponse("test ok")



# url(r'^demoview/$', views.DemoView.as_view())
                  # 装饰器名       被装饰的方法名
@method_decorator(my_decorator, name='get')
class DemoView(View):
    """定义类视图"""


    def get(self, request):

        return HttpResponse("get请求业务逻辑")

    def post(self, request):
        return HttpResponse("post请求业务逻辑")


    # 需要给类视图中多个方法（非全部）添加装饰器时：
    # @method_decorator(my_decorator)
    # def demo1(self, request):
    #     return  HttpResponse("demo1")
    #
    # @method_decorator(my_decorator)
    # def demo2(self, request):
    #     return  HttpResponse("demo")


# url(r'^template_view/$', views.TemplateView.as_view())
class TemplateView(View):

    def get(self, request):

        context = {
            "name": "Kakashi",
            "alist": [1, 2, 3],
            "adict":{"age": 18}
        }
                    # request     模板名字
        return render(request, 'index.html', context=context)