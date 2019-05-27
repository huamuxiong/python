#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 14:40
# @Author  : leyton
# @Site    : 
# @File    : test1.py
# @Software: PyCharm

from selenium import webdriver
driver = webdriver.Chrome()  # 打开浏览器

driver.get("http://www.scholat.com")  # 地址
print(driver.title)
