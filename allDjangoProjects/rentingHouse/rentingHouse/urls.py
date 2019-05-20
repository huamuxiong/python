"""rentingHouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin

import xadmin
from django.conf.urls import url, include
from apps.index.views import *
from rentingHouse.settings import STATIC_ROOT, MEDIA_ROOT
from django.views import static

urlpatterns = [
    url('^xadmin/', xadmin.site.urls),
    url('^', include('index.urls')),
    url('^homelink/', include('homelink.urls')),
    # url('^static/(?P<path>.*)$', static.serve, {'document_root': STATIC_ROOT}),

    url(r'^media/(?P<path>.*)$',static.serve,{"document_root":MEDIA_ROOT},name='media'),

    # 富文本
    url(r'^ueditor/', include('DjangoUeditor.urls')),
]

# handler404 = 'index.views.page_not_found'
# handler500 = 'index.views.page_error'