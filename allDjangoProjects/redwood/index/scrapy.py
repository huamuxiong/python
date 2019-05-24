# -*- coding: utf-8 -*-
from io import BytesIO

from django.shortcuts import render
from .models import RedWood
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from PIL import Image
import os


# from fake_useragent import UserAgent

import requests
import urllib.request
from bs4 import BeautifulSoup


from index.base import fileNewName, fenye

def jiaju_index(request):
    '''爬虫页面'''
    jiaju_list = RedWood.objects.all().order_by('-create_time')
    if jiaju_list:
        # paginator = Paginator(jiaju_list, 10)
        # page = request.GET.get('page')
        # page_obj = paginator.get_page(page)
        page = request.GET.get('page')
        page_obj = fenye(jiaju_list, page, 10)

        return render(request, 'redwoodscrapy/index.html', {'page_obj': page_obj})
    else:
        return render(request, 'redwoodscrapy/index.html')

def jiaju_spider(request):
    '''开始爬虫'''
    if request.method == 'POST':
        url = 'http://www.meilele.com/keywords/hongmujiaju/'
        redwood_spider = RedWoodSpider(url)

        redwood_spider.get_max_page()  # 获取最大页数
        redwood_spider.parse_page()  # 解析当前页（获取每一页的数据）
        redwood_spider.save_data_to_model()  # 保存数据

    return HttpResponseRedirect('/jiajuspider/')


class RedWoodSpider(object):
    def __init__(self, url):
        self.useragent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
        # self.ua = UserAgent(use_cache_server=False)
        self.headers = {"User-Agent": self.useragent}
        self.data = list()
        self.url = url

    def get_max_page(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            max_page = soup.select('b[class="i-num"]')[1].get_text().strip()  # 获取页码
            return max_page
        else:
            print("请求失败 status:{}".format(response.status_code))
            return None

    def parse_page(self, urllib2=None):
        max_page = self.get_max_page()
        for i in range(1, int(max_page) + 1):
            url = "{}/list-p{}/?from=page#p".format(self.url, i)
            response = requests.get(url, headers=self.headers)
            response.encoding = "utf-8"
            soup = BeautifulSoup(response.text, 'html.parser')
            ul = soup.find_all("ul", class_="list-goods clearfix")
            li_list = ul[0].select("li")
            for li in li_list:
                detail = dict()

                # try-except 内是爬取图片
                try:
                    img = li.find('img').get('data-src')  # 获取图片的地址
                    if img is None:
                        img = li.find('img').get('src')  # 由于有些img标签没有data-src, 改为src，保证爬取的每个都有图片

                    img = 'http:'+ img  # 由于网站内图片不提供http协议，自己加上
                    filename = fileNewName()  # 由于爬的img名称太长，给图片重新起一个名字（没有后缀）

                    detail['img'] = 'images/redwood/' + filename + '.' + img.split('.')[-1]  # images/redwood/xxx.jpg(.png,...)
                    urllib.request.urlretrieve(img, detail['img'])  # 下载图片并保存在本地
                except:
                    continue
                detail['price'] = li.select('span[class="m-count JS_async_price"]')[0].get_text()
                content = li.select('a[class="d-name"] span')[0].get_text()
                content1 = content.split('\t')
                content2 = list(filter(not_empty, content1))
                detail['title'] = ' '.join(content2)
                detail['type'] = int(typett(content2[1][:4]))
                self.data.append(detail)
                # detail['img'] = 'images/redwood/moren.jpg'


    def save_data_to_model(self):
        for item in self.data:
            # RedWood.objects.create(**item)
            new_item = RedWood()
            new_item.title = item['title']
            new_item.price = item['price']
            new_item.type = item['type']
            new_item.img = item['img']
            new_item.save()


def not_empty(s):
    return s and s.strip()

def typett(name):
    id = 0
    if name == '传统中式':
        id = 0
    elif name == '中式风格':
        id = 2
    else:
        id = 1
    return id
