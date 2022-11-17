from django.contrib import admin
from data.models import PassRate
from data.models import Distribution

# Register your models here.
class PassRateAdmin(admin.ModelAdmin):
    """
    创建PassRateAdmin类，继承于admin.ModelAdmin
    """
    #  配置展示列表，在版块下的列表展示
    list_display = ('title','date','subject','rate')
    # 配置过滤查询字段，在版块下右侧过滤框
    list_filter = ('title','date')
    # 配置可以搜索的字段，在版块下右侧搜索框
    search_fields = (['title','date','subject'])
    ordering = ('-created_at',)  # 定义列表显示的顺序，负号表示降序
    fieldsets = (
        (None, {
            'fields': ('title','date','subject','rate')
        }),
    )

class DistributionAdmin(admin.ModelAdmin):

    #  配置展示列表，在版块下的列表展示
    list_display = ('title','date','score','percentage')
    # 配置过滤查询字段，在版块下右侧过滤框
    list_filter = ('title','date')
    # 配置可以搜索的字段，在版块下右侧搜索框
    search_fields = (['title','date','score'])
    ordering = ('-created_at',)  # 定义列表显示的顺序，负号表示降序
    fieldsets = (
        (None, {
            'fields': ('title','date','score','percentage')
        }),
    )

# 绑定模型到管理后台
admin.site.register(PassRate, PassRateAdmin)
admin.site.register(Distribution, DistributionAdmin)