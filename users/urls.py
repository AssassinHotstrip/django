"""定义users应用的路由信息"""

from django.conf.urls import url
from users import views

# 在urlpatterns定义当前应用的所有路由
urlpatterns = [
    # 格式： url(r'^路径', views.视图),
    url(r'^users/index/$', views.index,  name="users:reverse_demo"), # 此处只是指定视图函数名称。函数index后不嫩添加括号
    # 路由的匹配顺序是从上到下的
    url(r'^users/sayhello/$', views.say_hello),
    url(r'^users/say/$', views.say),

]