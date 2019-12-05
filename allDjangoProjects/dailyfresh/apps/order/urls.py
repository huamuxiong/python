

from django.urls import path

from order.views import OrderPlaceView,OrderCommitView, \
    OrderPayView, CheckPayView, CommentView

urlpatterns = [
    # 显示提交页面
    path('place', OrderPlaceView.as_view(), name='place'),
    # 订单创建
    path('commit', OrderCommitView.as_view(), name='commit'),
    # 订单支付
    path('pay', OrderPayView.as_view(), name='pay'),
    # 支付结果
    path('check', CheckPayView.as_view(), name='check'),
    # 评论
    path('comment/<str:order_id>', CommentView.as_view(), name='comment'),

]
