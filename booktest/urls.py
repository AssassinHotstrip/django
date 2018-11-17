from rest_framework.routers import DefaultRouter


# 创建路由器
from booktest import views


urlpatterns = [ ]


router = DefaultRouter()
router.register(r'books', views.BookInfoViewSet)
urlpatterns += router.urls