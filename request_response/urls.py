from django.conf.urls import url

from request_response import views

urlpatterns = [

    # url(r'^weather/[a-z]+/\d{4}/$', views.weather),
    # 利用正则组提取url参数(位置参数)
    url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),

# 利用正则组提取url参数(关键字参数) 正则分组别名必须跟对应的参数名一致
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),

    # 演示提取查询字符串
    url(r'^query_str/$', views.query_str),

    # 演示提取请求体中的表单数据
    url(r'^query_form/$', views.query_form),

    # 演示提取查询非表单数据
    url(r'^body_json/$', views.body_json),

    # 演示获取请求头信息
    url(r'^request_head/$', views.request_head),

    # 演示常规响应操作
    url(r'^response_demo/$', views.response_demo),

    # 演示响应json数据
    url(r'^response_json/$', views.response_json),

    # 演示路由的命名空间和反向解析,name为给路由起别名以便于反向解析
    url(r'^reverse_demo/$', views.reverse_demo, name="request_response:reverse_demo"),

    # 演示重定向
    url(r'^redirect_demo/$', views.redirect_demo),

    # cookie缓存数据读写
    url(r'^cookie_demo/$', views.cookie_demo),

    # session缓存数据读写
    url(r'^session_demo/$', views.session_demo),
]
