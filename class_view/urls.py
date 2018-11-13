from django.conf.urls import url
from class_view import views



urlpatterns = [
    # url(正则路由， 函数视图)
    # as_view():内部根据请求自动分发方法，找到对象中的方法，把方法转为函数
    # DemoView是一个类，不是函数，需要用as_view（）转为函数
    url(r'^demoview/$', views.DemoView.as_view()),

    # 在路由中用装饰器装饰as_view返回的结果,但此方法会把类视图中所有方法都装饰
    # url(r'^demoview/$', views.my_decorator(views.DemoView.as_view())),

    # 加载模板
    url(r'^template_view/$', views.TemplateView.as_view()),
]