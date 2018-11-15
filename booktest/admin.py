from django.contrib import admin
from booktest.models import BookInfo,HeroInfo
from django.contrib import admin

# Register your models here.

# 修改页面标题信息
admin.site.site_header = '豹子书城'
admin.site.site_title = '豹子书城MIS'
admin.site.index_title = '欢迎使用豹子书城MIS'


# 关联对象                         （以块展示）
class HeroInfoStackInline(admin.StackedInline):
    model = HeroInfo  # 要编辑的对象
    extra = 1  # 附加编辑的数量



# 模型在站点中的展示管理
class BookInfoAdmin(admin.ModelAdmin):
    # 每页显示数据条数
    list_per_page = 2
    actions_on_top = True  # 操作选项在顶部显示
    # actions_on_bottom = True  # 操作选项在底部显示
    list_display = ["id", "btitle", "format_pub_date", "bread", "bcomment"]


    # 设置编辑可以修改的字段（默认全部能修改）
    # fields = ['btitle', 'bpub_date']  # 该列表之外的字段不能修改


    fieldsets = [
        # ("组名", {"key": ["该组包含的字段1","该组包含的字段2" ...]})
        ("基础", {"fields": ["btitle", "bpub_date", "image"]}),
        ("高级", {
            "fields": ["bread", "bcomment"],
            "classes": ("collapse",)  # 表示折叠显示（默认为不折叠）,需要修改时才打开设置（类似于各app的高级设置）
        })

    ]

    # 在编辑页面关联所有英雄数据
    inlines = [HeroInfoStackInline]



@admin.register(HeroInfo)  # 利用装饰器将模型和站点进行绑定
class HeroInfoAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ["id", "hname", "hgender", "hcomment",  "hbook", "read"]

    list_filter = ["hbook", "hgender"] # 添加按照书名或性别过滤的过滤器（默认为多重过滤效果，之前的过滤效果会保留）
    search_fields = ["hname"]  # 添加搜索器




# 把模型和站点进行绑定
admin.site.register(BookInfo, BookInfoAdmin)  #方式一：注册的同时绑定
# admin.site.register(HeroInfo)  # 方式二：装饰器（见上）





