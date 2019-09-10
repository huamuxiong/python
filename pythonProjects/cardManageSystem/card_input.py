# -*- coding: utf-8 -*-
def input_card_info(dict_value, tip_message):

    """输入名片信息

    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
    # 1. 提示用户输入内容
    result_str = input(tip_message)

    # 2. 针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:

        return result_str
    # 3. 如果用户没有输入内容，返回 `字典中原有的值`
    else:

        return dict_value