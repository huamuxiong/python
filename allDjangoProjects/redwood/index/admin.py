from django.contrib import admin
from .models import RedWood, Users, UserAdvice, UserCollect, UserComment, NewsInformation
# Register your models here.

class RedWoodAdmin(admin.ModelAdmin):
    '''家具管理'''
    fields = ('title', 'price', 'img', 'type', 'state')  # 编辑显示
    list_display = ('title', 'img', 'price', 'state')  # 列表显示
    search_fields = ('title', 'price')  # 搜索
    list_per_page = 10  # 每页显示条数
    list_editable = ['state']  # 可编辑
    fk_fields = ('state')  # 设置显示外键
    list_filter = ('state',)  # 过滤器
    date_hierarchy = ('create_time')  # 详细时间分层筛选　


class UsersAdmin(admin.ModelAdmin):
    '''用户管理'''
    list_display = ('username', 'email', 'headimg', 'isActive')

class UserAdviceAdmin(admin.ModelAdmin):
    '''用户建议管理'''
    pass

class UserCollectAdmin(admin.ModelAdmin):
    '''用户收藏管理'''
    pass

class UserCommentAdmin(admin.ModelAdmin):
    '''用户评论管理'''
    pass

class NewsInformationAdmin(admin.ModelAdmin):
    '''新闻资讯管理'''
    pass

admin.site.register(RedWood, RedWoodAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(UserAdvice, UserAdviceAdmin)
admin.site.register(UserComment, UserCommentAdmin)
admin.site.register(UserCollect, UserCollectAdmin)
admin.site.register(NewsInformation, NewsInformationAdmin)

admin.site.site_header = '宏兴红木家具销售系统'
admin.site.site_title = '宏兴红木家具销售系统'