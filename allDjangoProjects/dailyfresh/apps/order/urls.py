

from django.urls import path

from order.views import OrderPlaceView,OrderCommitView

urlpatterns = [
    # 显示提交页面
    path('place', OrderPlaceView.as_view(), name='place'),
    path('commit', OrderCommitView.as_view(), name='commit'), # 订单创建
]
