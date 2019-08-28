#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

from werkzeug.routing import BaseConverter
from flask import session, jsonify, g

from ihome.utils.response_code import RET


# 定义正则转换器
class ReConverter(BaseConverter):
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(ReConverter, self).__init__(url_map)
        # 保存正则表达式
        self.regex = regex


# 定义检验登陆状态的装饰器
def login_required(view_func):
    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        # 判断用户的登陆状态
        user_id = session.get('user_id')

        # 如果用户是登陆的，执行视图函数
        if user_id is not None:
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            # 未登录，返回未登录的信息
            return jsonify(errno=RET.SESSIONERR, errmsg='用户未登录')

    return wrapper


def xrange(start, end=None, step=1):
    if end == None:
        end = start
        start = 0
    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step
    else:
        return 'step can not be zero'

