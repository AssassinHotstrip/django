from django.conf.urls import url
from rest_framework.routers import DefaultRouter



from booktest import views
# from booktest import views_old


urlpatterns = [
    # # 使用APIView实现“获取所有图书信息”窗口
    # url(r"^books/$", views.BooksAPIView.as_view()),

    # # 使用GenericAPIView实现“获取所有/单个图书信息”窗口
#     url(r"^books/$", views.BookListView.as_view()),
#     url(r"^books/(?P<pk>\d+)$", views.BookDetailView.as_view()),

    # 使用GenericAPIView与Mixin实现“获取所有/单个图书信息”窗口
    # url(r"^books/$", views.BookListView.as_view()),
    # url(r"^books/(?P<pk>\d+)$", views.BookDetailView.as_view()),
    # # 使用GenericAPIView与Mixin实现“获取所有/单个图书信息”窗口
    # url(r"^books/create/$", views.BookCreatelView.as_view()),

    # 使用GenericViewSet获取所有/单一图书信息
    # url(r"^books/$", views.BookAPIViewSet.as_view({'get': 'list'})),
    # url(r"^books/(?P<pk>\d+)$", views.BookAPIViewSet.as_view({'get': 'retrieve'})),

    # 使用GenericViewSet+Mixin获取所有/单一图书信息
    # url(r"^books/$", views.BookAPIViewSet.as_view({'get': 'list'})),
    # url(r"^books/(?P<pk>\d+)$", views.BookAPIViewSet.as_view({'get': 'retrieve'})),

    # 使用ReadOnlyModelViewSet视图集获取只读信息
    # url(r"^books/$", views.BookAPIViewSet.as_view({'get': 'list'})),
    # url(r"^books/(?P<pk>\d+)$", views.BookAPIViewSet.as_view({'get': 'retrieve'})),

    # 使用ModelViewSet视图集获取只读信息(不全)
    # url(r"^books/$", views.BookAPIViewSet.as_view({'get': 'list', 'post':'create'})),
    # url(r"^books/(?P<pk>\d+)$", views.BookAPIViewSet.as_view({'get': 'retrieve'})),

]



# 创建路由器
router = DefaultRouter()
router.register(r'books', views.BookInfoViewSet)
urlpatterns += router.urls

