# -*- coding: utf-8 -*-
__author__ = 'leyton'
__date__ = '2019/4/15 0015 11:04'

from django import template
register = template.Library()  # 模板支持

from django.utils.safestring import mark_safe

@register.simple_tag
def circle_page(curr_page, loop_page):
    offset = abs(curr_page - loop_page)
    if offset < 4:
        if curr_page == loop_page:
            page_ele = '<li class="active"><a href=?page=%s>%s</a></li>'%(loop_page, loop_page)
        else:
            page_ele = '<li><a href=?page=%s>%s</a></li>' % (loop_page, loop_page)
        return mark_safe(page_ele)

    else:
        return ''
