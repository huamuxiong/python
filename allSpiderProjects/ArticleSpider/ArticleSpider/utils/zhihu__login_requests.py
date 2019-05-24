#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 17:51
# @Author  : leyton
# @Site    : 
# @File    : zhihu__login_requests.py
# @Software: PyCharm

import requests

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"
header = {
    'HOST': 'www.zhihu.com',
    'Referer': 'https://www.zhihu.com',
    'User-Agent': agent
}

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies.txt')

def get_xsrf():


    response = session.post('https://www.zhihu.com/signup?next=%2F', headers=header)
    return response.cookies['_xsrf']


def zhihu_login(account, password):
    # 知乎登陆
    if re.match('^1\d{10}', account):
        print('手机号登陆')
        post_url = "https://www.zhihu.com/api/v3/oauth/sign_in"
        post_data = {
            "X-Xsrftoken": get_xsrf(),
            'phone_num': account,
            'password': password
        }
        response_text = session.post(post_url, data=post_data, headers=header)
        session.cookies.save()

zhihu_login('15132788746', 'My..,962464')