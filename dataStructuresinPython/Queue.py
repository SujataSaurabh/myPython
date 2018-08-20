#	SuGo, 20 August 2018
#	Queue implementation along with the basic operations

class Queue:
	def __init__(self):
		self.items =[]
	
	def inQueue(self, data):
		self.items.insert(0, data)

	def outQueue(self):
		if self.items == []:
			print("Empty")
			return
		else:
			return self.items.pop()
	
	def printQueue(self):
		if self.items == []:
			print("Stack empty!!")
		else:	
			while(self.items):
				print(Queue.outQueue(self))

#	*****
Q = Queue()
Q.inQueue(1)
Q.inQueue(2)
Q.inQueue(3)

Q.printQueue()
