# 用DRF视图来定义视图
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin, CreateModelMixin
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.viewsets import ViewSet, GenericViewSet,ReadOnlyModelViewSet,ModelViewSet


from booktest.models import BookInfo
from .serializers import BookInfoSerializer




class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """添加操作"""
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # detail为False 表示路径名格式应该为 books/latest/
    @action(methods=['get'], detail=False)
    def latest(self, request):
        """
        返回最新的图书信息
        """
        book = BookInfo.objects.latest("id")
        serializer = self.get_serializer(book)
        return Response(serializer.data)


    # detail为True，表示路径名格式应该为 books/{pk}/read/
    @action(methods=['put'], detail=True) # detail为true则接收pk
    def read(self, request, pk):
        """
        修改图书的阅读量数据
        """
        book = self.get_object()
        book.bread = request.data.get("bread")
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)




class BookAPIViewSet(ModelViewSet):
    """"使用ModelViewSet实现五个基本操作"""
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

#
# class BookAPIViewSet(ReadOnlyModelViewSet):
#     """"使用ReadOnlyModelViewSet视图集获取只读信息"""
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer


# class BookAPIViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
#     """"使用Mixin+GenericViewSet视图集获取列表数据和单一数据"""
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer


# class BookAPIViewSet(GenericViewSet):
#     """"使用GenericViewSet视图集获取列表数据和单一数据"""
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer
#
#
#     def list(self, request):
#         books = self.get_queryset()
#         serializer = self.get_serializer(books, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk):
#         book = self.get_object()
#         serializer = self.get_serializer(book)
#
#         return Response(serializer.data)





class BookListView(ListAPIView):
    """使用ListAPIView来实现 获取所有图书信息 接口"""
    #  1.指定查询集
    queryset = BookInfo.objects.all()
    #  2.指定序化的类
    serializer_class = BookInfoSerializer

# class BookListView(ListModelMixin, GenericAPIView):
#     """使用GenericAPIView与Mixin来实现 获取所有图书信息 接口"""
#     #  1.指定查询集
#     queryset = BookInfo.objects.all()
#     #  2.指定序化的类
#     serializer_class = BookInfoSerializer
#
#     def get(self, request):
#
#         return self.list(request)


class BookDetailView(RetrieveAPIView):
    """使用RetrieveAPIView来实现 获取单个图书信息 接口"""
    #  1.指定查询集
    queryset = BookInfo.objects.all()
    #  2.指定序化的类
    serializer_class = BookInfoSerializer

# class BookDetailView(RetrieveModelMixin, GenericAPIView):
#     """使用GenericAPIView与Mixin来实现 获取单个图书信息 接口"""
#     #  1.指定查询集
#     queryset = BookInfo.objects.all()
#     #  2.指定序化的类
#     serializer_class = BookInfoSerializer
#
#     def get(self, request, pk):
#
#         return self.retrieve(request, pk)


class BookCreatelView(CreateModelMixin, GenericAPIView):
    """使用GenericAPIView与Mixin来实现 新建图书信息 接口"""
    #  1.指定查询集
    queryset = BookInfo.objects.all()
    #  2.指定序化的类
    serializer_class = BookInfoSerializer


    def get(self, request):

        return self.create(request)


class BooksAPIView(APIView):
    """使用APIView来实现 获取所有图书信息 接口"""

    def get(self, request):
        """
        GET/books
        :param request:
        :return:
        """
        # 1.获取查询集
        qs = BookInfo.objects.all()
        # 2.序列化
        serializer = BookInfoSerializer(qs, many=True)
        # 3.返回响应
        return Response(serializer.data)