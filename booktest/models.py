from django.db import models

# Create your models here.

# 定义图书模型类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    # 加完此字段之后,在迁移之前,一定要先安装 pillow 不然就报错
    # upload_to :指定上传图片的具体路径, 基于MEDIA_DIR 路径（static_files/media/booktest）
    # 如果模型已经迁移建表后,并且表已经有记录,后期又临时追加新的字段时,一定要注意新字段必须设置一个默认值,或为空
    # ImageField将来会自动生成相应的表单 让我们可以上传
    image = models.ImageField(upload_to='booktest', verbose_name='图片', null=True)


    class Meta:
        db_table = 'tb_books'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称（去掉此句后会以复数形式显示为“图书s”）


    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle


    def format_pub_date(self):
        """格式化时间"""
        # 更改显示格式
        return self.bpub_date.strftime("%Y-%m-%d")
    format_pub_date.short_description = "发布日期"  # 修改标题
    format_pub_date.admin_order_field = 'bpub_date'  # 指定按照bpub_date排序


# 定义英雄模型类
class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')



    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname

    def read(self):
        """显示英雄关联的图书阅读量"""
        # 利用外检获取到图书的阅读量
        return self.hbook.bread
    read.short_description = "阅读量"  # 修改显示标题
    read.admin_order_field = "hbook__bread"  # 指定排序方式按照hbook.bread







# class HeroInfo(models.Model):
#     GENDER_CHOICES = (
#         (0, 'female'),
#         (1, 'male')
#     )
#     hname = models.CharField(max_length=20, verbose_name='名称')
#     hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
#     hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
#     hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
#     is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
#
#     class Meta:
#         db_table = 'tb_heros'
#         verbose_name = '英雄'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.hname


