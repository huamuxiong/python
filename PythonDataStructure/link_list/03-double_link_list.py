# coding: utf-8


class Node:
	"""节点"""
	def __init__(self, elem):
		self.elem=elem
		self.next=None
		self.prev=None

class DoubleLinkList:
	"""双链表"""
	def __init__(self, node=None):
		self.__head=node

	def is_empty(self):
		return self.__head is None

	def length(self):
		cur = self.__head
		count = 0
		while cur is not None:
			count += 1
			cur=cur.next
		return count

	def travel(self):
		cur = self.__head
		while cur is not None:
			print(cur.elem, end=" ")
			cur = cur.next
		print('')

	def add(self, item):
		node = Node(item)
		if self.is_empty():
			self.__head=node
		else:
			node.next = self.__head
			self.__head = node
			node.next.prev = node

	def append(self, item):
		node = Node(item)
		if self.is_empty():
			self.__head=node
		else:
			cur = self.__head
			while cur.next is not None:
				cur = cur.next
			node.prev = cur
			cur.next = node
			

	def insert(self, pos, item):
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			cur = self.__head
			count = 0
			while count < (pos-1):
				count += 1
				cur = cur.next
			node =Node(item)
			node.next=cur
			node.prev=cur.prev
			cur.prev.next=node
			cur.prev=node

	def remove(self, item):
		node = Node(item)
		cur = self.__head
		while cur is not None:
			if cur.elem == item:
				if cur == self.__head:
					self.__head = cur.next
					if cur.next:
						cur.next.prev = None
				else:
					cur.prev.next = cur.next
					if cur.next:
						cur.next.prev = cur.prev
				break
			else:
				cur=cur.next

	def search(self, item):
		pass

if __name__ == "__main__":
	dll = DoubleLinkList()
	print(dll.is_empty())

	print(dll.length())

	dll.add(3)
	dll.travel()

	dll.add(4)
	dll.travel()

	dll.append(2)
	dll.travel()

	dll.append(5)
	dll.travel()

	dll.insert(2, 34)
	dll.travel()

	dll.insert(100, 100)
	dll.travel()

	dll.insert(-3, -3)
	dll.travel()

	dll.remove(-3)
	dll.travel()

	dll.remove(100)
	dll.travel()

	dll.remove(34)
	dll.travel()


