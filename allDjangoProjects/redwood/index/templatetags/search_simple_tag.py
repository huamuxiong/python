# -*- coding: utf-8 -*-

from django import template
from django.utils.safestring import mark_safe

register = template.Library()
@register.simple_tag #注册simple_tag
def action_all(current_url, index):  #接收当前url和对应的位置参数
    url_part_list = current_url.split('-')   # 根据“-”进行分割
    if index == 2:  # 如果是视频等级
        if url_part_list[index] == "0.html":   # 如果选择的是全部
            temp = "<a href='%s' class='on'>全部</a>"  # 添加 “active”属性
        else:
            temp = "<a href='%s'>全部</a>"

        url_part_list[index] = "0.html"
    else:
        if url_part_list[index] == "0":
            temp = "<a href='%s' class='on'>全部</a>"
        else:
            temp = "<a href='%s'>全部</a>"

        url_part_list[index] = "0"

    href = '-'.join(url_part_list)  # 处理后的列表再拼接成url字符串

    temp = temp % (href,)# 生成对应的a标签
    return mark_safe(temp) # 返回原生html


@register.simple_tag
def action(current_url, item, index):
    # videos-0-1.html
    # item: id name
    # video-   2   -0.html
    url_part_list = current_url.split('-')

    if index == 2:
        if str(item['id']) == url_part_list[2].split('.')[0]:  # 如果当前标签被选中
            temp = "<a href='%s' class='on'>%s</a>"
        else:
            temp = "<a href='%s'>%s</a>"

        url_part_list[index] = str(item['id']) + '.html'  # 拼接对应位置的部分url

    else:
        if str(item['id']) == url_part_list[index]:
            temp = "<a href='%s' class='on'>%s</a>"
        else:
            temp = "<a href='%s'>%s</a>"

        url_part_list[index] = str(item['id'])

    ur_str = '-'.join(url_part_list)  # 拼接整体url
    temp = temp % (ur_str, item['name'])  # 生成对应的a标签
    return mark_safe(temp)  # 返回安全的html