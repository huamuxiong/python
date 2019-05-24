# -*- coding: utf-8 -*-

# 防止重名覆盖，写一个函数用来生成文件名,其中年月日时分秒以毫秒的形式展示
import random
import time

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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

def fenye(contact, page, num):
    '''
    分页操作
    :param contact: 要分页的数据---model
    :param page: 传过来的页码
    :return: page 码对应的数据
    '''
    paginator = Paginator(contact, num)  # 每页显示10 条
    try:
        contacts = paginator.page(page)  # 获取传过来的page码的数据
    except PageNotAnInteger:
        contacts = paginator.page(1)  # 不是整数显示第一页
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)  # 没有page参数时显示全部页码
    return contacts


def price(price_id, *args, **kwargs):
    if price_id == 1:
        price_list = [2000]
    elif price_id == 2:
        price_list = [2000, 4000]
    elif price_id == 3:
        price_list = [4000, 6000]
    elif price_id == 4:
        price_list = [6000, 8000]
    elif price_id == 5:
        price_list = [8000, 10000]
    elif price_id == 6:
        price_list = [10000, 20000]
    elif price_id == 7:
        price_list = [20000]
    return price_list


