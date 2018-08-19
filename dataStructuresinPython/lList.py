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
	def nthNode(self, nPos):
		count = 1
		temp = self.head
		while(temp):
			if(count == nPos):
				return temp.data
			else: 
				temp = temp.next	
				count+=1
		print("counter out of bound!")
		return
	def nthNodeFromLast(self, nthLast):
		leng = 0
		temp = self.head
		while(temp):
			temp = temp.next
			leng+=1
		itemPos = leng-nthLast+1
		#print("itemPos -- ", itemPos) 
		counter = 1
		temp = self.head
		while(temp):
			if(counter == itemPos):
				return temp.data
			else:
				#print("value skipped == ", temp.data)
				temp = temp.next
				counter+=1
	def countRepeat(self, item):
		counter = 0 
		temp = self.head
		while(temp):
			if(temp.data == item):
				counter +=1
			temp = temp.next
		return counter

	def swapNodes(self, xNode, yNode):
		if (xNode == yNode):
			return 
		prevX = None
		prevY = None
		tempX = self.head 	# temp can also be referered as the current pointer
		while(tempX and tempX.data == xNode):
			prevX = tempX
			tempX = tempX.next
		tempY = self.head
		while(tempY and tempY.data == yNode):
			prevY = tempY
			tempY = tempY.next
		if (tempX == None or tempY ==None):
			return
		if (prevX == None):
			self.head = tempY
		else:
			prevX.next = tempY
		if (prevY == None):
			self.head = tempX
		else:
			prevY.next = tempX
		temp 	   = tempX.next
		tempX.next = tempY.next
		tempY.next = temp
		print("swapped pointers!")

	def moveLast2Front(self):
		temp = self.head
		while(temp.next):
			prev = temp
			temp = temp.next
		prev.next = None
		temp.next = self.head
		self.head = temp

	def segregateEvenOdd(self):
		temp = self.head
		llOdd = linkedList()  # link list ot store odd numbers only
		llEven = linkedList() # to store even numbers only
		while(temp):

			# 	prepare the linked list with even numbers
			
			if(temp.data %2 == 0):
				print("even ", temp.data)
				if(llEven.head is None):
					print("First even is Nil")
					llEven.head = temp
					#llEven.head.next   = None
				else:
					print("inserted in Even ", temp)
					llEven.insert_atFirst(temp)
						
			#	prepare the linked list with odd numbers
		
			else:
				print("odd ", temp.data)
				if(llOdd.head is None):
					print("First odd is Nil ")
					llOdd.head  = temp
					#llOdd.head.next  = None
				else:	
					print("inserted in Odd ", temp)
					llOdd.insert_atFirst(temp)
			temp = temp.next	
		# 	traverse even linked list as the odd list has to be appended to it
			print("traversing both Even and Odd...")
			
			llEven.traverse()
			llOdd.traverse()
			evenTmp  = llEven.head
			print("evenTmp", evenTmp)
			while(evenTmp):
				evenTmp = evenTmp.next
			evenTmp.next = llOdd.head
			return evenTmp

#	def detectLoop(self):
#		temp = self.head
#		while(temp):
#			if(temp.next == None):
#				return False
#			else:	
#				prev = temp
#				temp = temp.next
#				if()
#		return True



#	** test **
#	Start with the empty list
llist = linkedList()
llist.head = Node(1)
sec   	   = Node(2)
third 	   = Node(3)
four	   = Node(4)
five	   = Node(5)

llist.head.next = sec
sec.next   = third
third.next = four
four.next  = five
#five.next  = sec
#llist.traverse()
#print("inserting after specific node")
llist.insert_atPos(2, 6)
#print("inserting at first")
llist.insert_atFirst(10)
llist.insert_atFirst(100)
#print("inserting at end")
#llist.insert_atEnd(10)
#llist.delete_atNode(20)
llist.traverse()
#llist.delete_linkList()
#llist.traverse()
print("length of link llist -- ")
count = llist.length_linkList()
print(count)
#print("Searching item 10 in the list!")
#print(llist.search_linkList(10))
#print("Searching item 90 in the list!")
#print(llist.search_linkList(90))
#print("Third node is-- ", llist.nthNode(3))
#print("from Last the item is ", llist.nthNodeFromLast(3))
#print("10 is repeated ", llist.countRepeat(100), "times")
#print("Loop info == ", llist.detectLoop())
print("Swapping Nodes 2 and 3")
#llist.swapNodes(2, 6)
#print("List after swapping ... ")
llist.moveLast2Front()
llist.traverse()
llist.segregateEvenOdd()
llist.traverse()
