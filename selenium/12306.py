#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 14:44
# @Author  : leyton
# @Site    : 
# @File    : 12306.py
# @Software: PyCharm

# 测试12306订票
import time

from selenium import webdriver
driver = webdriver.Chrome()

# 设置窗口大小
driver.set_window_size(1080, 600)

# 设置全局操作超时时间
driver.implicitly_wait(10)

# 打开网址
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
# 打开登陆地址  F12 找到登陆的链接
driver.find_element_by_id('login_user').click()
driver.find_element_by_class_name('login-hd-account').click()

# time.sleep(1)

# 输入用户名和密码
driver.find_element_by_id('J-userName').send_keys('15132788746')
driver.find_element_by_id('J-password').send_keys('My_962464')
# print("continue")

time.sleep(15)  # 睡眠 5 秒用来输入验证码
# 点击登陆按钮
# driver.find_element_by_id('J-login').click()
# print('111')

# time.sleep(15)
# 根据链接的文本定位元素

# ul = driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul')
# lis = ul.find_element_by_xpath('li')
# print('aaaa')

# 手动选择单程

# 选择往返
driver.find_element_by_id('wf_label').click()
time.sleep(3)

# 出发地选择
driver.find_element_by_id('fromStationText').click()
time.sleep(2)
driver.find_element_by_css_selector('[title=上海]').click()

# 选择目的地
time.sleep(3)
driver.find_element_by_id('toStationText').click()
time.sleep(2)
driver.find_element_by_css_selector('[title=昆明]').click()
#
# print('aaaaaa')

# 选择出发时间
time.sleep(3)
driver.find_element_by_id('train_date').click()
time.sleep(2)
driver.find_element_by_css_selector('body > div.cal-wrap > div:nth-child(1) > div.cal-cm > div:nth-child(29) > div').click()

# 选择返程时间
time.sleep(3)
driver.find_element_by_id('back_train_date').click()
time.sleep(2)
driver.find_element_by_css_selector('body > div.cal-wrap > div:nth-child(1) > div.cal-cm > div:nth-child(31) > div').click()

# 选择车次类型
time.sleep(3)
driver.find_element_by_css_selector('#_ul_station_train_code > li:nth-child(1)').click()



try:
    # 点击查询按钮
    time.sleep(3)
    driver.find_element_by_id('query_ticket').click()
    e = driver.find_element_by_id('5l000G137751_AOH_KOM')
    e.click()
    if e.text in ['无', '--']:
        print('无票')
        time.sleep(1)
    else:
        print('yes')
        # 点击预订
        driver.find_element_by_css_selector('#ticket_5l000G137751 > td.no-br > a').click()
        # 选择购票人
        time.sleep(1)
        driver.find_element_by_css_selector('#normal_passenger_id > li:nth-child(1) > label').click()

        # 输入预订人
        # 点击提交订单
        time.sleep(1)
        driver.find_element_by_css_selector('#submitOrder_id').click()
        # 确定
        time.sleep(2)
        driver.find_element_by_css_selector('#qr_submit_id').click()

except:
    pass



