# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import datetime
import re

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def get_nums(value):
    """匹配value值中的数字，没有返回 0 """
    match_re = re.match('.*(\d+).*', value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


def add_hmx(value):
    return value + 'hmx'

def date_convert(value):
    """转换时间格式"""
    try:
        ftime_css = datetime.datetime.strftime(value, "%Y/%m/%d").date()
    except Exception as e:
        ftime_css = datetime.datetime.now().date()
    return ftime_css

def remove_comment_tags(value):
    if '评论' in value:
        return ""
    else:
        return value

def return_value(value):
    return value

class ArticleItemLoder(ItemLoader):
    # 自定义itemloder  默认输出列表中的第一个
    default_output_processor = TakeFirst()


class JobBoleArticleItem(scrapy.Item):
    # title = scrapy.Field(
    #     input_processor=MapCompose(lambda x:x+'leyton', add_hmx)
    # )
    title = scrapy.Field()
    ftime = scrapy.Field(
        input_processor=MapCompose(date_convert),
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_img_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )  # settings中配置下载 url 用于下载图片
    front_img_path = scrapy.Field()
    zan_count = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    shoucang_count = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_count = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(',')
    )
    content = scrapy.Field()
