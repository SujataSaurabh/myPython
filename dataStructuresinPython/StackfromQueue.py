#	SuGo, 20 August 2018
#	Implement Stack using single queue

class Queue:
	def __init__(self):
		self.items = []
	
	def inQ(self, data):
		print("Entering Que push")
		self.items.insert(0, data)
	
	def outQ(self):
		if(self.items != []):
			print("Entering Que pop")
			return self.items.pop()
		else:
			print("No items found")
			return
		
	def isEmpty(self):
		return (len(self.items) == 0)

class StackvonQ:
	def __init__(self):
		self.Q = Queue()

	def push(self, data):
		print("Entering StckQ push")
		self.Q.inQ(data)
	
	def pop(self):
		print("Entering StackQ pop")
		return self.Q.outQ()


#		****
SQ = StackvonQ()
SQ.push(1)
SQ.push(2)
SQ.push(3)

while(SQ):
	print(SQ.pop())
