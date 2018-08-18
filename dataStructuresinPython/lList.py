#	SuGo, 17 August 2018
#	Implements a linked list

class Node:
	def __init__(self, data):
	# intiliaze the node object 
		self.data = data 	# Assign data
		self.next = None	# Initialize next as NULL
class linkedList:
	def __init__(self):
	# Initialize the linked list 
		self.head = None
	
	def traverse(self):
			temp = self.head
			if(temp == None):
				print('No items found!')
				return
			else:
				while (temp):
					print(temp.data)
					temp = temp.next
			
	#
	def insert_atFirst(self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head    = newNode

	def insert_atPos(self, prev, data):
		print("Entering insert function")
		new_Node = Node(data)
		temp     = self.head
		while(temp):
			if(temp.data == prev):
				new_Node.next  = temp.next
				temp.next      = new_Node
				return 
			else:
				temp = temp.next
		print("node not found")
		return
	#	
	def insert_atEnd(self, data):
		newNode = Node(data)
		temp    = self.head
		while(temp.next):
			temp = temp.next		
		temp.next = newNode	
	def delete_atNode(self, val):
		temp = self.head
		while(temp):
			if(temp.data == val):
				break
			prev = temp
			temp = temp.next
		if(temp == None):
			print("Node not found!")
			return
		else:
			prev.next = temp.next
			temp = None	
	
	def delete_linkList(self):
		temp =self.head
		self.head = None
		while(temp):
			current = temp.next
			del  temp.data
			temp = current
	def length_linkList(self):
		count = 0
		temp = self.head
		while(temp):
			count +=1	
			temp = temp.next
		return count
	def search_linkList(self, val):
		temp = self.head
		while(temp):
			if(temp.data == val):
				return True
			else:
				temp = temp.next
		return False
	
#	** test **
#	Start with the empty list
llist = linkedList()
llist.head = Node(1)
sec   	   = Node(2)
third 	   = Node(3)

llist.head.next = sec
sec.next   = third
llist.traverse()
print("inserting after specific node")
llist.insert_atPos(2, 6)
print("inserting at first")
llist.insert_atFirst(100)
print("inserting at end")
llist.insert_atEnd(10)
llist.delete_atNode(20)
llist.traverse()
llist.delete_linkList()
llist.traverse()
print("length of link llist -- ")
count = llist.length_linkList()
print(count)
print("Searching item 10 in the list!")
print(llist.search_linkList(10))
print("Searching item 90 in the list!")
print(llist.search_linkList(90))


