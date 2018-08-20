#	SuGo, 20 August 2018
#	Implement queue using stacks 
# Note: To implement the queue operations, we use two stacks Stack1 and Stack2.
#	First empty Stack1 to Stack2. Then push an item in Stack1. After pushing an item in Stack1
#	again empty all the items in Stack1 from Stack2

class QueuevonStacks:
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()

	def inQueue(self, data):
		self.stack1.push(data)
	
	def outQueue(self):
		if(self.stack2.isEmpty()):
			while(not self.stack1.isEmpty()):
				item  = self.stack1.Pop()
				self.stack2.push(item)
#		while(self.stack2.items != []):
		return self.stack2.Pop()
#	def printQueue(self):
#		while(self.stack2.items != []):
#			print(QueuevonStacks.outQueue(self))

class Stack:
	def __init__(self):
		self.items = []

	def push(self, data):
		self.items.append(data)

	def Pop(self):
		return self.items.pop()
	
	def isEmpty(self):
		return (len(self.items) == 0)
		

#	****

QS = QueuevonStacks()
QS.inQueue(0)
QS.inQueue(2)
QS.inQueue(3)
QS.inQueue(10)


print(QS.outQueue())

