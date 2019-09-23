

from django.urls import path
from .views import register, regiseter_handle


urlpatterns = [
    path('register/', register, name='register'),  # 注册页面
    path('register_handle', regiseter_handle, name='regiseter_handle'),  # 注册业务

]
