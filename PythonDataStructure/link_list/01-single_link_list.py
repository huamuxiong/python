

'''单链表'''


class Node:
	'''一个节点包括当前地址和链接下一个节点的地址，
	'''
	def __init__(self, elem):
		self.elem = elem  # 当前节点
		self.next = None  # 当前节点指向的下一个节点的地址

class SingleLinkList:
	def __init__(self, node=None):
		'''只需要一个头结点'''
		self._head = node  # 头节点指向第一个节点，如果没有节点则指向None

	def is_empty(self):
		'''判断链表是否为空'''
		return self._head == None  # 如果头结点指向None，则表示链表为空

	def length(self):
		'''求链表的长度'''
		# 需要遍历整个链表，增加一个游标cur
		cur = self._head  # 默认指向头结点，从头节点开始遍历
		count = 0  # 长度计数器，默认只能是0个（链表为空）
		''' 判断条件：
			因为cur指向的是self._head，有两种结果
			cur = None
			cur.next = None
			至于条件是哪个，因为cur指向的是头结点地址，所以当头结点指向None时
			而不是cur.next，想想，如果头结点指向空，就没有next了
		'''
		while cur != None:
			count += 1
			cur = cur.next  # 游标指向下一个地址
		return count  # 如果链表为空，直接返回0

	def travel(self):
		'''遍历链表'''
		'''游标指向头结点，当游标指向空时遍历结束'''
		cur = self._head
		while cur != None:
			print(cur.elem, end=" ")
			cur = cur.next
		print('')

	def add(self, item):
		''' 链表头部插入
    		先获取该节点与next的地址
    		让该节点的next指向头结点
    		再让头结点的next指向插入的节点
		'''
		node = Node(item)
		node.next = self._head
		self._head = node

	def append(self, item):
		'''链表尾部插入'''
		node = Node(item)
		''' 先判断链表是否为空，如果空，则头结点指向插入的节点
			否则，遍历列表，当游标的next指向空时，让游标的next指向插入的节点即可
		'''
		if self.is_empty():
			self._head = node
		else:
			cur = self._head
			while cur.next != None:  # 这里为什么不是cur != None?考虑next
				cur = cur.next
			cur.next = node

	def insert(self, pos, item):
		''' 指定位置插入
   			假设pos=3
   			思路：遍历到3的位置时让item节点的next连接3的next
   			3的next连接item
   			特殊情况：头插法和尾插法已实现，直接调用
		'''
		if pos < 0:  # -2
			self.add(item)
		elif pos > (self.length()-1):  # 长度为3，但插入的位置为5
			self.append(item)
		else:
			pre = self._head
			count = 0
			while count < (pos-1):
				count += 1
				pre = pre.next
			node = Node(item)
			node.next = pre.next
			pre.next = node

	def remove(self, item):
		'''删除节点'''
		cur = self._head  # 游标
		pre = None  # 游标的上一个节点地址，既然游标指向了头结点，pre自然指向None
		# 遍历链表
		while cur != None:
			# 判断是否找到，否则游标移动
			if cur.elem == item:
				# 需要判断是否是头结点,如果是，直接让头结点指向空
				if cur == self._head:
					self._head = None
				else:
					pre.next = cur.next
				break
			else:
				# 这个时候到底是pre先移动还是cur先移动
				# 如果是cur先移动，那么pre就移动不了了，所以先移动pre
				pre = cur
				cur = cur.next

	def search(self, item):
		''' 查找节点是否存在'''
		cur = self._head
		while cur != None:
			if cur.elem == item:  # 如果找到，返回True
				return True
			else:  # 否则移动游标
				cur = cur.next
		return False

if __name__ == '__main__':
	sll = SingleLinkList()
	print(sll.is_empty())
	sll.append(1)
	sll.travel()
	sll.add(44)
	sll.travel()
	sll.insert(-3, 55)
	sll.travel()
	sll.insert(3, 66)
	sll.travel()
	sll.insert(33, 77)
	sll.travel()
	sll.remove(66)
	sll.travel()
	sll.search(55)
	sll.travel()
	