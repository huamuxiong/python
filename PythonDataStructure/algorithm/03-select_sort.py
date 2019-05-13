# coding: utf-8

"""
选择排序
在乱序中选择最小的进行交换位置，放在前边
假如现在有序列 [54, 26, 93, 17, 77, 31, 44, 55, 20]
假设最小值是第一个元素，即 54
从第二个往后找到最小的元素，即17
让 54 和 17 交换位置，即 [17, 26, 93, 54, 77, 31, 44, 55, 20]
因为17已经是最小的数了，就没有必要再进行比较了，
让最小值等于第二个数，即26，重复上述操作
从第三个往后找到最小的元素，即20
让 26 和 20 交换位置，即 [17, 20, 93, 54, 77, 31, 44, 55, 26]

。。。

需要重复多少次：
序列有 n 个数，重复 n-1 次
"""

def select_sort(alist):
	# 在做外层，共交换n-1遍
	for j in range(len(alist)-1):  # 共交换n-1次
		# 现做内层，走一遍
		max_index = j
		for i in range(j+1, len(alist)):  # 找最小的元素，要从 j 的下一个开始找到最后一个 
			if alist[max_index] > alist[i]:
				max_index = i  # 记录列表中最小元素的下标
		alist[j], alist[max_index] = alist[max_index], alist[j]


if __name__ == '__main__':
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	select_sort(alist)
	print(alist)


