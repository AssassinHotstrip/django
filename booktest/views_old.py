# import json
# from django.views import View
# from django.http import JsonResponse,HttpResponse
# from  rest_framework.viewsets import ModelViewSet
#
#
# from .models import BookInfo
# from .serializers import BookInfoModelSerializer

"""
GET      /books/        提供所有记录
POST     /books/        新增一条记录

GET      /books/<pk>/   提供指定id的记录
PUT      /books/<pk>/   修改指定id的记录
DELETE   /books/<pk>/   删除指定id的记录

响应数据    JSON
"""
#
#
# class BookInfoViewSet(ModelViewSet):
#     """定义书籍视图集"""
#     queryset = BookInfo.objects.all()  # 给视图指定查询集
#     serializer_class = BookInfoModelSerializer