

from django.urls import path
from cart.views import CartAddView, CartInfoView, CartUpdateView, CartDeleteView
urlpatterns = [
    # 添加购物车
    path('add/', CartAddView.as_view(), name='add'),
    # 显示购物车
    path('', CartInfoView.as_view(), name='show'),
    # 更新购物车
    path('update/', CartUpdateView.as_view(), name='update'),
    # 删除购物车记录
    path('delete/', CartDeleteView.as_view(), name='delete'),
]
