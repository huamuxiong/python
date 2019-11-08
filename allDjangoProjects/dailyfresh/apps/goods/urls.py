

from django.urls import path
from .views import IndexView, DetailView, ListView


urlpatterns = [
    # 主页
    path('', IndexView.as_view(), name='index'),
    # 详情页
    path('detail/<str:goods_id>/', DetailView.as_view(), name='detail'),
    # 列表页
    path('list/<str:type_id>/<str:page>/', ListView.as_view(), name='list'),


]
