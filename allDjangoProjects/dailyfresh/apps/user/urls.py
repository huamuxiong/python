
# user.urls
from django.conf.urls import url
from django.urls import path
# from .views import register, regiseter_handle
from .views import RegisterView, ActiveView, LoginView, LogoutView,\
    UserInfoView, UserOrderInfoView, UserAddressView

urlpatterns = [
    # path('register/', register, name='register'),  # 注册页面
    # path('register_handle', regiseter_handle, name='regiseter_handle'),  # 注册业务

    path('register/', RegisterView.as_view(), name='register'),  # 注册逻辑
    path('active/<str:token>/', ActiveView.as_view(), name='active'),  # 账户激活逻辑
    path('login/', LoginView.as_view(), name='login'),  # 登陆逻辑
    path('logout/', LogoutView.as_view(), name='logout'),  # 退出逻辑

    path('', UserInfoView.as_view(), name='user'),
    path('order/', UserOrderInfoView.as_view(), name='order'),
    path('address/', UserAddressView.as_view(), name='address'),


]
