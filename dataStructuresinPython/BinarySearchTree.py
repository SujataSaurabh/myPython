#	@SuGo, 8 August 2018
#	Implementation of Binary search tree
#	reference: https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
class Node:
	def __init__(self, key):
		self.left = self.right = None
		self.value = key
	
def insert(root, node):
	if root is None:
		root = node
	else:
		if root.value<node.value:
			if root.right is None:
				root.right = node
			else:	
				insert(root.right,node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)
## traversal (INORDER)
def inorder(root):   # Left Node Right
	if root:
		inorder(root.left)
		print(root.value)
		inorder(root.right)
def preorder(root):  # Node Left Right
	if root:
		print(root.value)
		preorder(root.left)
		preorder(root.right)
def postorder(root):  # Left Right Node
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.value)
def minNode(root):
	if root is None:
		return root
	else:	
		if root.left is not None:
			root = root.left
	return root
# 		**** 	test	****
root = Node(50)
insert(root, Node(20))
insert(root, Node(40))
print("\n INORDER")
inorder(root)
print("\n PREORDER")
preorder(root)
print("\n POSTORDER")
postorder(root)
minNode(root)
