#!/usr/bin/env python
# -*- coding: utf-8 -*-

from celery import Celery

from ihome.libs.yuntongxun.sms import CCP

# 定义celery对象
celery_app = Celery("ihome", broker="redis://127.0.0.1:6379/1")

# 定义任务
@celery_app.task
def send_sms(to, datas, temp_id):
    """发送短信的异步任务"""
    ccp = CCP()
    ccp.sendTemplateSMS(to, datas, temp_id)
