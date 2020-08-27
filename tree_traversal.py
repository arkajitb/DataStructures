class Node:
	def __init__(self,val):
		self.childleft = None
		self.childright = None
		self.nodedata = val

# creating an instance of the Node class to construct the tree 

root = Node(1)
root.childleft = Node(2)
root.childright = Node(3)
root.childleft.childleft = Node(4)
root.childleft.childright = Node(5)

def InOrder(root):
	if root: 
		InOrder(root.childleft)
		print(root.nodedata)
		InOrder(root.childright)

InOrder(root)

def PreOrder(root):
	if root:
		print(root.nodedata)
		PreOrder(root.childleft)
		PreOrder(root.childright)

#PreOrder(root)

def PostOrder(root):
	if root:
		PostOrder(root.childleft)
		PostOrder(root.childright)
		print(root.nodedata)

#PostOrder(root)
