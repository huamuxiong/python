# -*- coding: utf-8 -*-

"""
有 n 个人按顺序围成一圈开始报数，每当报的数是 3 的倍数就出局，问最后剩下的是原来的第几个人
如 n = 9, 则剩下的是 1
如 n = 8, 则剩下的是 7
如 n = 7, 则剩下的是 4
"""


# 自定义输入人数
# p_count = int(input(">>> "))
p_count = 7
# 对人数排队：列表
p_list = list(range(1, p_count+1))
# 初始化报数
num = 0
# 只要列表中的人数大于1个，就进行报数
while len(p_list) > 1:
    # 拷贝一份列表，内循环使用
    p_list_cp = p_list[:]
    # 内循环，对cp列表进行循环报数
    for i in range(0, len(p_list_cp)):
        num += 1
        # 如果报数为3，则出局
        if num % 3 == 0:
            p_list.remove(p_list_cp[i])


print(p_list)