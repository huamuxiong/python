from django.db.models import Q
from django.shortcuts import render
from .models import HouseInfo
from .forms import HouseChoiceForm
# from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# from fake_useragent import UserAgent
import requests
from urllib import request
from bs4 import BeautifulSoup
import re

from index.views import fileNewName
from index.models import Village, Location

# Create your views here.


# 主页面
def house_index(request):
    form = HouseChoiceForm()
    # 按add_date发布时间降序排序
    house_list = HouseInfo.objects.all().order_by('-add_date')
    if house_list:
        # 对获取到的数据进行分页，每页显示20条数据
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(house_list, 1, request=request)

        page_obj = p.page(page)

        return render(request, 'homelink/index.html',{'page_obj': page_obj, 'form': form})
    else:
        return render(request, 'homelink/index.html', {'form': form})


# 爬虫请求--post--开始爬取
def house_spider(request):
    if request.method == 'POST':
        form = HouseChoiceForm(request.POST)
        if form.is_valid():
            # 获取选择的三个选项
            district = form.cleaned_data.get('district')  # 地区
            price = form.cleaned_data.get('price')  # 价格
            bedroom = form.cleaned_data.get('bedroom')  # 居室
            # 要爬去的地址url + 条件
            url = 'https://bj.lianjia.com/zufang/{}/{}{}'.format(district, bedroom, price)

            # 开始爬去，初始化对象，并调用相应的方法，最后保存在数据库中
            home_spider = HomeLinkSpider(url)  # 实例化对象
            # try:
            home_spider.get_max_page()  # 获取最大页数
            home_spider.parse_page()  # 解析当前页（获取每一页的数据）
            home_spider.save_data_to_model()  # 保存数据
            # except:
            #     pass
            return HttpResponseRedirect('/homelink/')
    else:
        return HttpResponseRedirect('/homelink/')


class HomeLinkSpider(object):
    def __init__(self, url):
        # self.ua = UserAgent()
        self.useragent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
        # self.headers = {"User-Agent": self.ua.random}
        self.headers = {"User-Agent": self.useragent}
        self.data = list()
        self.url = url

    def get_max_page(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            a = soup.select('div[class="content__pg"]')

            max_page = a[0].get("data-totalpage")
            return max_page
        else:
            print("请求失败 status:{}".format(response.status_code))
            return None

    # 获取每一页的数据
    def parse_page(self):
        max_page = self.get_max_page()
        for i in range(1, int(max_page) + 1):
            url = "{}pg{}/".format(self.url, i)
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            ul = soup.find_all("div", class_="content__list")
            li_list = ul[0].select("div")
            for li in li_list:
                detail = dict()
                try:
                    detail['img_address'] = li.find('img').get('data-src')
                    _img_name = fileNewName()  # 调用fileNewName()生成新的名字
                    detail['img_address1'] = 'static/renthouseImg/' + _img_name + '.' + detail['img_address'].split('.')[-1]
                    request.urlretrieve(detail['img_address'], detail['img_address1'])  # 下载图片
                except:
                    continue
                detail['title'] = li.select('p[class="content__list--item--title twoline"]')[0].get_text().strip()
                # 海淀-海淀北部新区 / 57m² / 南 北 / 2室1厅1卫 中楼层（4层）
                house_info = li.select('p[class="content__list--item--des"]')[0].get_text()
                house_info_list = house_info.split("/")

                house_info_address = house_info_list[0].strip().split('-')  # 昌平-霍
                detail['village'] = Village.objects.get(name=house_info_address[0]).id  # 昌平
                try:
                    name = house_info_address[1]
                    # print('name: ', name)
                    detail['location'] = Location.objects.get(name=house_info_address[1]).id  # 霍营
                    # print('%s-%s '%(detail['location'], detail['location'].id))
                except:
                    pass
                    # detail['location'] = 1
                detail['area'] = house_info_list[1].strip()[:-1]  # 72m²
                detail['direction'] = house_info_list[2].strip()  # 南 北
                detail['bedroom'] = house_info_list[3].strip()  # 2室2厅1卫
                detail['floor'] = house_info_list[4].strip().replace(' ', '')  # 低楼层(6层)
                detail['release_time'] = li.select('p[class="content__list--item--time oneline"]')[0].get_text()  # 20天之前

                # 单价64182元/平米， 匹配64182
                unit_price = li.select('span[class="content__list--item-price"]')[0].get_text().strip().split(' ')
                detail['unit_price'] = unit_price[0]
                self.data.append(detail)

    # 将数据进行保存
    def save_data_to_model(self):
        for item in self.data:
            new_item = HouseInfo()
            new_item.title = item['title']
            new_item.village_id = item['village']
            new_item.location_id = item['location']
            new_item.bedroom = item['bedroom']
            new_item.area = item['area']
            new_item.direction = item['direction']
            new_item.floor = item['floor']
            new_item.release_time = item['release_time']
            new_item.unit_price = item['unit_price']
            _img = '/' + item['img_address1']
            new_item.img_address = _img
            new_item.save()

