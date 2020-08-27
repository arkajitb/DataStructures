class Node:
	def __init__(self,data):
		self.leftNode = None
		self.rightNode = None
		self.data = data

##.         1
#.        /    \
#.      2.      4
#.     /.\     / \
#.    3.  6   7   5
traversal = []
def PreOrder(leef):

	if leef:
		traversal.append(leef.data)
		PreOrder(leef.leftNode)
		PreOrder(leef.rightNode)

def InOrder(leef):
	if leef:
		InOrder(leef.leftNode)
		traversal.append(leef.data)
		InOrder(leef.rightNode)

def PostOrder(leef):
	if leef:
		PostOrder(leef.leftNode)
		PostOrder(leef.rightNode)
		traversal.append(leef.data)

if __name__ == '__main__':
	root = Node(1)
	root.leftNode = Node(2)
	root.rightNode = Node(4)
	root.leftNode.leftNode = Node(3)
	root.leftNode.rightNode = Node(6)
	root.rightNode.rightNode = Node(5)
	root.rightNode.leftNode = Node(7)
	PostOrder(root)
	print(traversal)
