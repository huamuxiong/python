# -*- coding: utf-8 -*-
import random
import time

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

__author__ = 'leyton'
__date__ = '2019/3/1 0001 17:01'

from django.shortcuts import render, redirect

# def checkLogin(func):
#     '''
#     查看session值来判断用户是否登录
#     :param func:
#     :return:
#     '''
#     def warpper(request, *args, **kwargs):
#         if request.session('user_id', False):
#             return func(request, *args, **kwargs)
#         else:
#             return redirect('/login')
#
#     return warpper


def houseType(addr):
    housetype = ''
    if addr == 'zufang':
        housetype = '租房'
    if addr == 'xinfang':
        housetype = '新房'
    if addr == 'ershoufang':
        housetype = '二手房'
    return housetype

# 获取当前时间
def getNowDateTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


# 防止重名覆盖，写一个函数用来生成文件名,其中年月日时分秒以毫秒的形式展示
def fileNewName():
    # 唯一时间
    timer = int(time.time() * 1000)

    # 生成大小写16位字母
    s = ''
    for i in range(16):
        s += random.choice([chr(random.randint(65, 90)), chr(random.randint(97, 122))])
    file = list(str(timer) + s)
    random.shuffle(file)
    file1 = ''.join(file)
    return file1


def price(price_id, *args, **kwargs):
    print('price: ', price_id, type(price_id))
    if price_id == 1:
        price_list = [1000]
    elif price_id == 2:
        price_list = [1000, 2000]
    elif price_id == 3:
        price_list = [2000, 3000]
    elif price_id == 4:
        price_list = [3000, 4000]
    elif price_id == 5:
        price_list = [4000, 5000]
    elif price_id == 6:
        price_list = [5000, 8000]
    elif price_id == 7:
        price_list = [8000]
    return price_list


def fenye(contact, page, num):
    '''
    分页操作
    :param contact: 要分页的数据---model
    :param page: page: 传过来的页码,num: 每页多少条
    :return: page 码对应的数据
    '''
    paginator = Paginator(contact, num)
    try:
        contacts = paginator.page(page)  # 获取传过来的page码的数据
    except PageNotAnInteger:
        contacts = paginator.page(1)  # 不是整数显示第一页
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)  # 没有page参数时显示全部页码
    return contacts




