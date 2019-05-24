# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path

# from .views import *
from index import views, scrapy

urlpatterns = [
    # 爬虫
    path('jiajuspider/', scrapy.jiaju_index, name='jiaju_index'),
    path('spider/', scrapy.jiaju_spider, name='jiaju_spider'),

    path('', views.index_views),  # 主页
    path('login/', views.login_views),  # 登录
    path('logout/', views.logout_views),  # 退出登录
    path('register/', views.register_views),  # 注册

    # 家具相关
    url(r'^jiaju/j-(?P<style1>\d+)-(?P<price1>\d+).html', views.jiaju_list_views, name='/jiaju/'),  # 家具列表
    url(r'^jiaju_info/(\d+)/', views.jiaju_info_views, name='jiajuinfo'),  # 家具详情页

    # 关注
    path('guanzhu/', views.guanzhu_views),
    # 新闻资讯
    path('news/', views.news_information_views),
    # 新闻资讯详情页
    path('newsinfo/', views.news_info_views),
    # 关于我们
    path('aboutus/', views.aboutus_views),
    # 联系我们
    path('contactus/', views.contactus_views),

    # 个人中心--个人资料页
    path('userinfo/', views.user_info_views),
    # 个人中新--修改密码
    path('userinfo/resetpassword/', views.reset_password_views),
    # 个人中心--个人资料--上传头像
    path('userinfo/upload_avatar/', views.upload_avatar_views),
    # 个人中心--收藏（关注）
    path('userinfo/usercollect/', views.user_collect_views),
    # 个人中心--浏览记录
    path('userinfo/userhistory/', views.user_history_views),
    # 评论页面
    path('comment/', views.comment_views),
    # 删除评论
    path('deletecomment/', views.del_comment_views),
    # 个人中心--评论
    path('userinfo/usercomment/', views.user_comment_views),
    # 个人中心--申诉建议
    path('userinfo/useradvice/', views.user_advice_views),
    # 错误页面
    path('error/', views.error_views),
]
