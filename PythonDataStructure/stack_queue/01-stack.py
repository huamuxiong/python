# coding: utf-8

class Stack:
	def __init__(self):
		self.__list = []

	def is_empty(self):
		'''判断是否为空'''
		return self.__list == []

	def push(self, item):
		"""压栈"""
		self.__list.append(item)

	def pop(self):
		"""出栈"""
		return self.__list.pop()

	def peek(self):
		'''返回栈顶元素'''
		if self.__list:
			return self.__list[-1]
		else:
			return None

	def size(self):
		'''返回栈元素的个数'''
		return len(self.__list)

if __name__ == '__main__':
	stack = Stack()
	print(stack.is_empty())

	stack.push(4)
	stack.push(5)
	stack.push(6)

	print(stack.pop())

	print(stack.peek())
	# print(stack.peek())
	# stack.peek()

	print(stack.size())

