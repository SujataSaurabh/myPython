#	SuGo, 20 August 2018
#	Implements a stack which performs middle element operations (find and delete middle) in O(1) time

# 	This stack can be implemented by using the doubly linked list

class Node:
	def __init__(self, data):
		self.item = data
		self.prev = None
		self.next = None

class midStack:
	def __init__(self):
		self.head = None
	
	def pushatFront(self, data):
		newNode = Node(data)
		if self.head == None:
			self.head = newNode
		else:
			self.head.prev = newNode
			newNode.next   = self.head
			self.head      = newNode

	def popfromFront(self): 
		data = self.head.item
		self.head = self.head.next
		return data
	
	def traverse(self):
		temp = self.head
		while(temp):
			#print(midStack.popfromFront(self))
			 print(temp.item)
			 temp = temp.next
	def countNodes(self):
		counter = 0
		temp = self.head
		while(temp):
			counter = counter+1
			temp = temp.next
		return counter
	
	def returnMid(self):
		lenList = ms.countNodes()
		counter = 0
		
		midNode = int((lenList+1)/2)
		if(lenList%2)==0: midNode = int(lenList/2)
		
		temp = self.head
		
		while(temp):
			if(counter == midNode):
				return temp.item
			else:	
				counter = counter+1
				temp = temp.next
		return
 
	def deleteMid(self):
		#temp = self.head
		lenList = ms.countNodes()
		counter = 0
		
		midNode = int((lenList+1)/2)
		if(lenList%2)==0: midNode = int(lenList/2)
		
		temp = self.head
		
		while(temp):
			if(counter == midNode):
				middleNode =  temp
				break
			else:	
				counter = counter+1
				temp = temp.next

		#midNode = midStack.returnMid(self)
		prevNode = middleNode.prev
		nextNode = middleNode.next
		prevNode.next = nextNode
		nextNode.prev = prevNode
		del middleNode

		
#		****
ms = midStack()
ms.head = Node(1)
sec     = Node(2)
third   = Node(3)

sec.next = third
sec.prev = ms.head
third.prev = sec
ms.head.next = sec

print("traversing the linked list...")
ms.traverse()

print("pushing 4 and 5 at the front")
ms.pushatFront(4)
ms.pushatFront(5)
print("traversing the new lisnk list ...")
ms.traverse()

print("Now popping 5 from the linked list ...")
print(ms.popfromFront())

print("traversing the linked list ...")
ms.traverse()

print("total number of nodes in the linked List:: ", ms.countNodes())
print("Middle item of the Linked list:: ", ms.returnMid())
print("traverse after mid delete ", ms.deleteMid())
ms.traverse()
