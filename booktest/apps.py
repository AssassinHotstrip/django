from django.apps import AppConfig


class BooktestConfig(AppConfig):
    name = 'booktest'  # 指定应用配置类（setting中所加载的类）
    verbose_name = "图书管理"  # Django中admin管理站显示的名字

