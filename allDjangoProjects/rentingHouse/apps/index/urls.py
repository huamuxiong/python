from django.conf.urls import url
from index.views import *


urlpatterns = [

    url('^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='active_code'),  # 注册激活链接
    url('^forget/$', ForgetUserPasswdView.as_view(), name='forget'),  # 忘记密码
    url('^reset/(?P<active_code>.*)/$', ResetPwdView.as_view(), name='reset_pwd'),  # 注册激活链接
    url('^modifypwd/$', ModifyPasswdView.as_view(), name='modify_pwd'),  # 忘记密码


    # url('^contact/$', ContactUsView.as_view(), name='contact'),
    # url('^contactsubmit/$', ContactUsSubmitView.as_view(), name='contact_submit'),

    url('^$', index_views),                # 首页
    url('^logout/$', logout_views),        # 退出
    url('^login/$', login_views),          # 登录
    url('^register/$', register_views),    # 注册
    url('^aboutus/$', aboutus_views),      # 关于我们
    url('^contactus/$', contactus_views, name='contact_submit'),  # 联系我们
    url('^news/', news_information_views),  # 新闻资讯
    url('^newsinfo/(\d+)', news_info_views),
    url('^fabu/$', fabu_views),            # 发布
    url('^fabu/upload/$', fabu_upload_views),  # 发布房源上传图片

    url('^userinfo/$', userinfo_views),                        # 个人中心--展示资料
    url('^userinfo/upload_avatar/$', upload_avatar_views),     # 个人中心--上传头像
    url('^userinfo/updateUserinfo/', updateUserinfo_views),    # 个人中心--修改个人信息
    url('^userinfo/reset_pwd/$', reset_pwd_views),             # 个人中心--修改密码
    url('^userinfo/user_guanzhu/$', user_guanzhu_views),       # 个人中心--关注
    url('^userinfo/user_history/$', user_history_views),       # 个人中心--我的足迹
    url('^userinfo/user_zhiding/$', user_zhiding_views),       # 个人中心--指定购房
    url('^userinfo/deleteZD/$', user_deleteZD_views),          # 个人中心--删除指定购房
    url('^userinfo/updateZD/$', user_updateZD_views),          # 个人中心--修改指定购房信息
    url('^userinfo/Supdate/$', user_Supdate_views),          # 个人中心--修改指定购房信息
    url('^userinfo/user_shenqing/$', user_shenqing_views),     # 个人中心--申请成为经纪人
    url('^userinfo/upload_zhaopian/$', upload_zhaopian_views), # 个人中心--申请经纪人上传照片
    url('^userinfo/wodefabu/$', wodefabu_views),               # 个人中心--我的房源发布列表
    url('^userinfo/updateFabu/', updateFabu_views),            # 个人中心--修改发布的信息界面
    url('^userinfo/deleteFabu/', deleteFabu_views),            # 个人中心--删除发布的信息
    url('^userinfo/advice/', advice_views),                    # 个人中心--我的申诉建议
    url('^userinfo/usercomment/', user_comment_views),        # 个人中心--我的评论列表
    url('^pro_zu/house-(?P<village_id>\d+)-(?P<location_id>\d+)-(?P<price_id>\d).html', pro_zu1_views, name='/pro_zu/'),  # 租房页面
    url('^pro_zu_info/(\d+)/$', pro_zu_info_views, name='prozuinfo'),       # 租房详情页面
    url('^guanzhu/$', guanzhu_views),               # 关注
    url('^comment/$', comment_views),               # 评论
    url('^deletecomment/', del_comment_views),     # 删除评论
    url('^zhidinggf', zhidinggf_views),             # 指定购房
    url('^zhiding/$', zhiding_views),                   # 指定购房---改后
    url('^zhiding/(?P<id>\d+)', zhiding2_views),
    url('^ajax-location/$', locationValue_views),     # 指定购房的二级联动---根据village的id值获取对应的位置信息

    # url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # url('^ajax_email/$', ajax_email_views),
]



