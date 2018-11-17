# from django.db.models import F, Sum
# from django.db.models import Q
# from django.shortcuts import render
# from booktest.models import BookInfo, HeroInfo
# #
# # Create your views here.
#
# # 操作：增加(方式一)
# book = BookInfo()
# book.btitle = '三国演义'
# book.bpub_date = '1876-10-10'
# book.save()
#
# # 操作：增加(方式二)
# book = BookInfo(
#     btitle = '西游记',
#     bpub_date= '1888-8-8'
# )
# book.save()
#
# # 操作：增加(方式三)
# BookInfo.objects.create(
# btitle = '火影忍者',
#     bpub_date= '1999-11-8'
# )
# # 此方式会返回结果：<BookInfo: 火影忍者>
#
#
#
#
# # 操作：查询
# # 查询所有
# BookInfo.objects.get(id=1)
#
# # 查询记录
# BookInfo.objects.count()
#
#
# # 过滤查询
# BookInfo.objects.filter(id=2)
#
#
# # 查询书名中包含“湖”的书名
# BookInfo.objects.filter(btitle__contains='湖')
#
#
# # 查询书名以“部”结尾的书籍
# BookInfo.objects.filter(btitle__endswith="部")
#
#
# # 查询书名不为空的书籍
# BookInfo.objects.filter(btitle__isnull=False)
#
#
# # 查询编号为3或5的书籍
# BookInfo.objects.filter(id__in=[3, 5])
#
#
# # 查询编号大于2的书籍
# BookInfo.objects.filter(id__gt=2)
#
#
# # 查询id不等于3的书籍
# BookInfo.objects.exclude(id=3)
#
#
# # 查询1980年发表的书籍
# BookInfo.objects.filter(bpub_date__year='1980')
#
#
# # 查询1888年8月8日发表的书籍
# BookInfo.objects.filter(bpub_date='1888-08-08')
#
#
# # 查询1990年1月1日后发表的书籍
# BookInfo.objects.filter(bpub_date__gt='1990-1-1')
#
#
# # 查询阅读量大于评论量的书籍
# BookInfo.objects.filter(bread__gt=F('bcomment'))
#
#
# # 查询阅读量大于2倍评论量的书籍
# BookInfo.objects.filter(bread__gt=F('bcomment')*2)
#
#
# # 查询阅读量大于20，或编号小于3的图书
# BookInfo.objects.filter(Q(bread__gt=20)|Q(id__lt=3))
#
#
# # 查询编号不等于3的书籍
# BookInfo.objects.filter(~Q(id=3))
#
#
# # 查询图书的总阅读量
# BookInfo.objects.aggregate(Sum('bread'))
#
#
# # 使用count时不使用aggregate()
# # 查询图书总量
# BookInfo.objects.count()
#
#
# # 按阅读量升序排序
# BookInfo.objects.all().order_by('bread')
#
#
# # 按阅读量降序排序
# BookInfo.objects.all().order_by('-bread')
#
#
# # 基础关联查询一对多
# # 查询编号为1的图书所有人物信息：
# book = BookInfo.objects.get(id=1)
# book.heroinfo_set.all()   # heroinfo为多的一方对象名字的小写
#
#
# # 基础关联查询多查一
# # 查询编号为1的英雄出自的书籍：
# hero = HeroInfo.objects.get(id=1)
# hero.hbook
#
#
# # 关联过滤查询一查多
# # 查询书名为“天龙八部”的所有人物信息
# HeroInfo.objects.filter(hbook__btitle="天龙八部")
#
#
# # 关联过滤查询多对一
# # 查询书籍中人物的描述包含“降龙”的书籍
# BookInfo.objects.filter(heroinfo__hcomment__contains="降龙")
#
#
#
# # 修改数据 方式一
# # 将“猪八戒”改为“猪悟能”
# hero = HeroInfo.objects.get(hname="猪八戒")
# hero.hname = '猪悟能'
# hero.save()
#
#
# # 修改数据 方式二
# # 将“沙悟净”改为“沙僧”
# HeroInfo.objects.filter(hname="沙悟净").update(hname="沙僧")
# HeroInfo.objects.filter(hname='沙悟净').update(hname='沙僧')
#
# # 删除  方式一
# hero = HeroInfo.objects.get(id=13)
# hero.delete()
#
# # 删除  方式二
# HeroInfo.objects.filter(id=12).delete()
