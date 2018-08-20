#	SuGo, 20 August 2018
#	Implements a stack and its basic operations

class Stack:
	def __init__(self):
		self.items = []

	def push(self, data):
		self.items.append(data)
	
	def pop(self):
		if self.items == []:
			print("Stack empty!!")
			return
		else:
			return self.items.pop()

	def printStack(self):
		while(self.items):
			print(self.pop())

#  test the class
s = Stack()
s.push(1)
s.push(2)
s.push(3)

s.printStack()
