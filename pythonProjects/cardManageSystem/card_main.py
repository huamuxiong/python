# -*- coding: utf-8 -*-

import card_tools

while True:

    # TODO(张三) 此位置显示菜单
    card_tools.show_menus()

    action_str = input("请输入代号：")
    print("您输入的是【%s】" % action_str)

    # 判断输入的是否是菜单中的代号
    if action_str in ['1', '2', '3']:
        # 3 中操作
        if action_str == '1':
            # 新增卡片
            card_tools.new_card()
        elif action_str == '2':
            # 显示全部
            card_tools.show_all()
        elif action_str == '3':
            # 查询名片
            card_tools.search_card()

    elif action_str == '0':
        # 退出
        break
    else:
        print("您输入的有误，请重新输入")