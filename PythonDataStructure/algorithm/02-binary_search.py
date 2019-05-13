# coding: utf-8


"""
二分查找算法
序列必须是有序的

加入现在有一个序列 [17, 20, 26, 31, 44, 54, 55, 77, 93]
需要查找的数据是item

思路：二分查找，顾名思义，将序列一分为二，
可以根据分成的两部分的中间值和要查找的值比较大小

如果item大于中间值，说明在第二部分
如果item小于中间值，说明在第一部分
如果item等于中间值，说明找到了
如果最后没找到，说明不在序列中

假设item=77
上述列表中的中间值为44（长度为偶数取中间的第二个数，地板除法）
第一次查找，77 > 44,所以在第二部分，中间值已经比较过了，就不要了
现在的列表[54, 55, 77, 93]

再重复上次的操作，此时中间值为77，
第二次查找，77 == 77 ，找到返回True

"""


def binary_search(alist, item):  # 接收两个参数，一个链表，一个要查找的值
	# 递归
	if len(alist) > 0:
		mid = len(alist) // 2  # 中间的值
		if alist[mid] == item:  # 如果中间值刚好等于item，说明找到了，返回True
			return True
		elif item > alist[mid]:  # 如果中间值小于item，说明在第二部分
			return binary_search(alist[mid+1:], item)  # 将第二部分列表递归
		else:
			return binary_search(alist[:mid], item)
	else:
		return False


def binary_search1(alist, item):
	# 非递归
	start = 0
	end = len(alist)-1
	
	while start <= end：
		mid = (end+start)//2
		if alist[mid] == item:
			return True
		elif alist[mid] < item:
			start = mid + 1
		else:
			end = mid - 1
	return False

if __name__ == '__main__':
	li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
	print(binary_search1(li, 31))



