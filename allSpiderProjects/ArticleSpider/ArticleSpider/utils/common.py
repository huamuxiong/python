#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 10:10
# @Author  : leyton
# @Site    : 
# @File    : common.py
# @Software: PyCharm

import hashlib


# 加密
def get_md5(url):
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()
