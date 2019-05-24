#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 18:48
# @Author  : leyton
# @Site    : 
# @File    : main.py
# @Software: PyCharm

from scrapy.cmdline import execute

import sys
import os

# print(os.path.dirname(os.path.abspath(__file__)))
# os.path.dirname(os.path.abspath(__file__))  # 当前项目的路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 设置在命令行执行 scrapy crawl spider名称
# 在windows系统上需要安装win32api
# 安装：pip install -i https://pypi.douban.com/simple pypiwin32
execute(['scrapy', 'crawl', 'jobbole'])
