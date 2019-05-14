# coding: utf-8

"""
快速排序

快速排序是对冒泡排序的升级版
假如现在有序列 [54, 26, 93, 17, 77, 31, 44, 55, 20]
可以以第一个数为基准，让后边比基准数小的在左边，大的在右边
重复上述操作

具体实现过程：
设立一个中间值（基准数）=第一个数
设立起始值和最后值分别对应序列的第一个数和最后一个数
让最后一个先与基准数比较大小，如果比基准数大，继续往左移动，否则与起始值交换位置，并停止移动
此时起始值开始移动，与基准数比较大小，如果比基准数小，继续往右移动，否则与最后值交换位置，并停止移动

到起始值与最后值相遇时都停止移动，并插入中间基准数
这样就完成了一次快速排序

此时基准数左边的都比基准数小，右边的都比基准数大，但都无序。让左右部分继续执行上述操作


结题过程：
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
min_value = 54
start = 空
end = 20

end先移动--> 20 < 54  将 end 赋值给start，即此时的序列为 [20, 26, 93, 17, 77, 31, 44, 55, ]，end处为空，停止移动
此时：
min_value = 54
start=20
end = 空

20 < 54，start 往右移动一步，
此时：
min_value = 54
start=26
end = 空

26 < 54，start 往右移动一步，
min_value = 54
start=93
end = 空

93 > 54  将 start 赋值给 end，即此时的序列为 [20, 26,  , 17, 77, 31, 44, 55, 93]，start 处为空，停止移动
此时：
min_value = 54
start = 空
end = 93

93 > 54，end 往左移动一步，
此时：
min_value = 54
start = 空
end = 55

55 > 54，end 往左移动一步，
此时：
min_value = 54
start = 空
end = 44

44 < 54，将 end 赋值给 start，即此时的序列为 [20, 26, 44, 17, 77, 31,  , 55, 93]，end 处为空，停止移动
此时：
min_value = 54
start = 44
end = 空

44 < 54，start 往右移动一步，
此时：
min_value = 54
start = 17
end = 空

17 < 54，start 往右移动一步，
此时：
min_value = 54
start = 77
end = 空

77 > 54，将 start 赋值给 end，即此时的序列为 [20, 26, 44, 17,  , 31, 77, 55, 93]，end 处为空，停止移动
此时：
min_value = 54
start = 空
end = 77

77 > 54， end 往左移动一步，
此时：
min_value = 54
start = 空
end = 31

31 < 54，将 end 赋值给 start，即此时的序列为 [20, 26, 44, 17, 31,  , 77, 55, 93]，end 处为空，停止移动
此时：
min_value = 54
start = 31
end = 空

31 < 54，start 往右移动一步
此时：
min_value = 54
start = 空
end = 空

此时 start = end 并同时都为空，谁都不移动了，此时将min_value插入到中间，由于start=end，赋值给谁都行
可让start=min_value
即此时的序列为 [20, 26, 44, 17, 31, 54, 77, 55, 93]

那么:
左边的序列为 [20, 26, 44, 17, 31]
右边的序列为 [77, 55, 93]

对左右再执行上述操作

"""

"""
那么第一次快速排序如何实现？

"""

"""
def quick_sort(alist):
	n = len(alist) - 1  # 列表的长度
	start = 0  # 开始值为列表的第一个元素
	end = n  # 最后值为列表的最后一个元素
	min_value = alist[start]  # 中间基准数
	print(alist[end], min_value)
	print(start, end)
	while start < end:
		# 如果最后一个值大于中间基准数，让最后一个值的索引往左移动一步，
		# 如果下一个的条件依然满足，就再往左一步，此时可用循环，
		# 但什么时候停下来呢，最坏的情况是遇到start时，即while start < end
		# 当条件 alist[end] > min_value 不满足时，alist[start]=alist[end]
		# 但是赋值操作是否应当在 while 循环条件内呢
		# 因为 while 中只有一个条件，
		# 但是 if 条件不满足时 while 仍然满足，就不会退出循环，无法完成赋值，所以应当是退出循环再赋值
		# 可将 while 与 if 合并，也就是当 alist[end] > min_value 不满足或 start < end 不满足时都退出循环执行下一步
		
		if alist[end] > min_value:
			end -= 1
	alist[start]=alist[end]

if __name__ == '__main__':
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	quick_sort(alist)
	print(alist)

"""


"""
def quick_sort(alist):
	n = len(alist) - 1  # 列表的长度
	start = 0  # 开始值为列表的第一个元素
	end = n  # 最后值为列表的最后一个元素
	min_value = alist[start]  # 中间基准数
	print(alist[end], min_value)
	print(start, end)

	# 左右移动又是一个循环的过程，那么结束条件是什么
	# 移动到start >= end 时以下不再移动
	while start < end:
		while start < end and alist[end] > min_value:
			end -= 1
		alist[start]=alist[end]

		# 同时可将 start 的移动写出来
		while start < end and alist[start] < min_value:
			start += 1
		alist[end]=alist[start]

	# 当 start < end 的条件不满足时，即当 start 和 end 相遇时退出循环，插入中间基准数min_value
	# 因为此时 start 和 end 都移动到了序列中间的某个地方，所以可以将min_value赋值给start或end所在的位置
	alist[start] = min_value
	# 此时的序列为 [20, 26, 44, 17, 31,      54,      77, 55, 93]

if __name__ == '__main__':
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	quick_sort(alist)
	print(alist)

"""

"""
def quick_sort(alist):
	n = len(alist) - 1  # 列表的长度
	start = 0  # 开始值为列表的第一个元素
	end = n  # 最后值为列表的最后一个元素
	min_value = alist[start]  # 中间基准数

	while start < end:
		while start < end and alist[end] > min_value:
			end -= 1
		alist[start]=alist[end]
		while start < end and alist[start] < min_value:
			start += 1
		alist[end]=alist[start]
	alist[start] = min_value
	# 此时的序列为 [20, 26, 44, 17, 31,      54,      77, 55, 93]
	# 可利用递归继续让左右两部分执行上述操作
	quick_sort(alist[:start-1])  # 左部分
	quick_sort(alist[start+1:])  # 右部分

	# 但是 start 和 end 就不再是原序列的索引了，我们应该操作原序列，
	# 我们让函数传 start 和 end，这样我们 start 和 end 的值就行了，而传递的序列还是 alist

if __name__ == '__main__':
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	quick_sort(alist)
	print(alist)

"""


"""
def quick_sort(alist, first, last):


	# n 作为参数传递过来，即last
	start = first  # 列表的第一个元素
	end = last  # 列表的最后一个元素
	min_value = alist[start]  # 中间基准数



	while start < end:
		while start < end and alist[end] > min_value:
			end -= 1
		alist[start]=alist[end]
		while start < end and alist[start] < min_value:
			start += 1
		alist[end]=alist[start]
	alist[start] = min_value
	# 此时的序列为 [20, 26, 44, 17, 31,      54,      77, 55, 93]
	# 可利用递归继续让左右两部分执行上述操作

	# 我们让函数传 start 和 end，这样我们 start 和 end 的值就行了，而传递的序列还是 alist
	quick_sort(alist, first, start-1)  # 左部分的开始值还是原序列的开始值，但是最后值是基准数的前一个索引
	quick_sort(alist, start+1, last)   # 右部分的开始值是基准数的后一个索引，最后值还是原序列的最后值


	# 考虑特殊情况， 
	# 1. 如果序列的长度小于 1 ，应直接返回序列，
	# 2. 序列中不只有一个54，我们让他往一边倒，可以让它到右部分，即 while start < end and alist[end] >= min_value ----> 大于等于
	# 看下一个 

if __name__ == '__main__':
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	quick_sort(alist, 0, len(alist)-1)
	print(alist)

"""

def quick_sort(alist, first, last):
	if first < last:
		start = first  # 列表的第一个元素
		end = last  # 列表的最后一个元素
		min_value = alist[start]  # 中间基准数

		while start < end:
			while start < end and alist[end] >= min_value:
				end -= 1
			alist[start]=alist[end]
			while start < end and alist[start] < min_value:
				start += 1
			alist[end]=alist[start]
		alist[start] = min_value
		quick_sort(alist, first, start-1)
		quick_sort(alist, start+1, last)
	return alist

if __name__ == '__main__':
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	# alist = [1]
	quick_sort(alist, 0, len(alist)-1)
	print(alist)



