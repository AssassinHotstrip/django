# 序列化：将模型转换为字典

from booktest.serializers import BookInfoSerializer,HeroInfoSerializer
from booktest.models import BookInfo,HeroInfo

"""反序列化测试代码"""




# json_dict = {"btitle": "三国无双django", "bpub_date": "1810-10-29", "bread":60, "bcomment":50}
# serializer =BookInfoSerializer(data=json_dict) #反序列化时，给data参数传递数据
# # serializer.is_valid()   # 必须先验证数据是否正确
# # serializer.errors  # 获取数据验证错误信息，返回字典
# serializer.is_valid(raise_exception=True) # 验证数据是否正确，异常自动抛出
# serializer.validated_data  #
#





"""序列化测试代码"""

# book = BookInfo.objects.get(id=1)  # 获取数据库中一个模型
# serializer = BookInfoSerializer(instance=book)  # 利用序列化器序列化
# serializer.data



# 序列化查询集中d额多个模型
# queryset = BookInfo.objects.all()  # 获取所有模型
# serializer = BookInfoSerializer(instance=queryset, many=True)  # 序列化,many为提醒序列化器获取多个
# serializer.data  # 获取序列化之后的字典


# 序列化英雄模型
# hero = HeroInfo.objects.get(id=1)
# serializer = HeroInfoSerializer(hero)
# serializer.data