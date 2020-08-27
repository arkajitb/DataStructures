#Access any of the elements of an array in O(1).
#Linked list doesn't have any order in the memory. The order is created by the data structure
#node class is a sub class of the linked list
class node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

class linked_list:
	def __init__(self):
		self.head = node()

	#function to append a new node to the end of the linked list
	def append(self,data):
		new_node = node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node


	#function to find the length of the linked list
	def total_nodes(self):
		cur = self.head
		total = 0
		while cur.next != None:
			total += 1
			cur = cur.next
		return total

	#helper function to display the current contents in the list
	def display(self):
		elems = []
		cur_node = self.head
		cur_node = cur_node.next
		while cur_node != None:
			elems.append(cur_node.data)
			cur_node = cur_node.next

	
	def get(self, index):
		if index >= self.total_nodes():
			print('error')
			return None
		cur_idx = 0
		cur_node = self.head
		while True:
			cur_node = cur_node.next
			if cur_idx == index:return cur_node.data
			cur_idx += 1
		print('elements', elems)

	def erase(self, index):
		if index >= self.total_nodes():
			print('error')
			return None
		cur_idx = 0
		cur_node = self.head
		while True:

			if cur_idx+1 == index:
				cur_node = cur_node.next
				cur_

			

my_list = linked_list()
my_list.append(11)
my_list.append(12)
my_list.append(13)
my_list.append(14)

my_list.display()

print("element at 2nd index", my_list.get(1))