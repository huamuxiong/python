

from django.urls import path
# from .views import register, regiseter_handle
from .views import RegisterView, ActiveView, LoginView

urlpatterns = [
    # path('register/', register, name='register'),  # 注册页面
    # path('register_handle', regiseter_handle, name='regiseter_handle'),  # 注册业务

    path('register/', RegisterView.as_view(), name='register'),  # 注册逻辑
    path('active/(?P<token>.*)/', ActiveView.as_view(), name='active'),  # 账户激活逻辑
    path('login/', LoginView.as_view(), name='login'),  # 登陆逻辑

]
