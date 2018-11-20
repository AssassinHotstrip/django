# 定义模型序列化器
from rest_framework import serializers

from .models import BookInfo

# class BookInfoModelSerializer(serializers.ModelSerializer):
#     """定义序列化器"""
#     class Meta:
#         model = BookInfo  # 给序列化器指定要映射的模型
#         fields = "__all__"  # 映射所有字段
        # fields = ['xx', 'xxx']  # 映射某几个字段



# 定义一个（继承自rest_framework.serializers.Serializer）序列化器


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label="ID", read_only=True)
    btitle = serializers.CharField(label="名称", max_length=20)
    bpub_date = serializers.DateField(label="发布日期", required=False)
    bread = serializers.IntegerField(label="阅读量", required=False)
    bcomment = serializers.IntegerField(label="评论量",required=False)
    image = serializers.ImageField(label="图片", required=False)
    # 一关联多外键序列化
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # many=True是告诉序列化器此字段有多个数
    heroinfo_set = serializers.StringRelatedField(read_only=True, many=True)  # many=True是告诉序列化器此字段有多个数


    def validate_btitle(self, value):
        """给单个字段额外增加校验逻辑"""
        # if 'django' not in value.lower():
        #     raise serializers.ValidationError("图书不是关于Django的")
        return value


    def validate(self, attrs):
        """验证多个字段"""
        bread = attrs['bread']
        bcomment = attrs['bcomment']
        if bread < bcomment:
            raise serializers.ValidationError('阅读量小于评论量')
        return attrs

    def create(self, validated_data):
        """新建"""

        return BookInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""

        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.save()
        return instance


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
    # 关联外键序列化
    hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)   #  返回关联对象id
    # hbook = serializers.PrimaryKeyRelatedField(label='图书', queryset=BookInfo.objects.all())
    # hbook = serializers.StringRelatedField(label='图书')  # 返回字符串
    # hbook = BookInfoSerializer()  # 返回整个信息