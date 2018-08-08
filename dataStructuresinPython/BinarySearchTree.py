#	@SuGo, 8 August 2018
#	Implementation of Binary search tree
'''
class BStree:
	def __init__(self):
		self.key = self.value = None
		self.left =self.right = None
	def __setItem__(self, key, value):
		if self.key == None:
			self.key = key
			self.value = value
		elif key == self.key:
			self.value = value
		elif key<self.key:
			if self.left:
				self.left[key] = value
			else:
				self.left = BStree(key, value)
		else:
			if self.right:
				self.right[key] = value
			else:
				self.right = BStree(key, value)
	def __getItem__(self, key):
		if self.key == None:
			return None
		elif key == self.key:
			return self.value
		elif key < self.key and self.left:
			return self.left[key]
		elif key > self.key and self.right:
			return self.right[key]
		else:
			return None
'''
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
def inorder(root):
	if root:
		inorder(root.left)
		print(root.value)
		inorder(root.right)
def preorder(root):
	if root:
		print(root.value)
		preorder(root.left)
		preorder(root.right)
def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.value)
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
