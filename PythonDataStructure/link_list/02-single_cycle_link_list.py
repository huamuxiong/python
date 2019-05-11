# 02-single_cycle_link_list.py

# 单向循环链表

class Node:
	def __init__(self, elem):
		self.elem = elem
		self.next = None

class SingleCycleLinkList:
	def __init__(self, node=None):
		self.__head=node
		if node:
			node.next=node  # 链表闭合

	def is_empty(self):
		return self.__head==None

	def length(self):
		if self.is_empty():
			return 0
		cur=self.__head
		count = 1
		while cur.next != self.__head:
			count += 1
			cur=cur.next
		return count

	def travel(self):
		'''遍历链表'''
		if self.is_empty():
			return 
		cur = self.__head
		while cur.next != self.__head:
			print(cur.elem, end=" ")
			cur=cur.next
		print(cur.elem)  # 打印最后一个节点

	def add(self, item):
		'''头插法'''
		node = Node(item)
		# 如果链表为空的话，头节点指向node，node节点的next在重新指向node形成闭合
		if self.is_empty():
			self.__head=node
			node.next=node
		else:
			cur=self.__head
			while cur.next != self.__head:
				cur=cur.next
			# 让node节点的next指向之前的第一个节点
			# 重新让head指向node成为头结点
			# 让最后一个的next指向头结点形成闭合
			node.next=self.__head
			self.__head=node
			cur.next=self.__head

	def append(self, item):
		'''尾插法'''
		node=Node(item)
		# 如果是空链表，让head指向node，再让node的next指向head形成闭合
		if self.is_empty():
			self.__head=node
			node.next=self.__head
		else:
			cur=self.__head
			while cur.next != self.__head:
				cur=cur.next
			# 让最后一个节点的next指向node，再让node的next指向head形成闭合
			cur.next=node
			node.next=self.__head

	def insert(self, pos, item):
		if pos <= 0:
			self.add(node)
		elif pos > (self.length()-1):
			self.append(node)
		else:
			pre=self.__head
			count=0
			while count < (pos-1):
				count += 1
				pre=pre.next
			node = Node(item)
			node.next=pre.next
			pre.next=node

	def remove(self, item):
		"""删除节点"""
		if self.is_empty():
			return

		cur = self.__head
		pre = None

		while cur.next != self.__head:
			if cur.elem == item:
				# 先判断此结点是否是头节点
				if cur == self.__head:
					# 头节点的情况
					# 找尾节点
					rear = self.__head
					while rear.next != self.__head:
						rear = rear.next
					self.__head = cur.next
					rear.next = self.__head
				else:
					# 中间节点
					pre.next = cur.next
				return
			else:
				pre = cur
				cur = cur.next
		# 退出循环，cur指向尾节点
		if cur.elem == item:
			if cur == self.__head:
				# 链表只有一个节点
				self.__head = None
			else:
				# pre.next = cur.next
				pre.next = self.__head

	def search(self, item):
		if self.is_empty():
			return False
		cur=self.__head
		while cur.next != self.__head:
			if cur.elem == item:
				return True
			else:
				cur=cur.next
		if cur.elem == item:
			return True
		return False

if __name__ == '__main__':
	scll = SingleCycleLinkList()
	print(scll.is_empty())
	print(scll.length())

	scll.add(2)
	scll.travel()

	scll.append(3)
	scll.travel()

	scll.append(4)
	scll.travel()

	# print(scll.search(3))

	scll.remove(2)
	scll.travel()


