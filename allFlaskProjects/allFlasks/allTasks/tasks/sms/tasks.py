#!/usr/bin/env python
# -*- coding: utf-8 -*-

from allTasks.tasks.main import celery_app
from allTasks.libs.yuntongxun.sms import CCP

# 定义任务
@celery_app.task
def send_sms(to, datas, temp_id):
    """发送短信的异步任务"""
    ccp = CCP()
    return ccp.sendTemplateSMS(to, datas, temp_id)
