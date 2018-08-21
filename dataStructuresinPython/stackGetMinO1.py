#	SuGo, 21 August 2018
#	This program implements a stack. This stack is special because it returns the minimum 
#	element of the stack in O(1) time and O(1) extra space.
#	webref: https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
# 	Still has to be corrected!!
class specialStack():
	def __init__(self):
		self.items = []
		self.minEle = 0

	def isEmpty(self):
		return self.items == []
	
	def setMin(self, item):
		self.minEle = item
	
	def push(self, data):
		if specialStack.isEmpty(self):
			self.items.append(data)
			self.minEle = data
			print("min ele", self.minEle)
		else:
			self.items.append(data)
			print("pushed ele is ", data)
			if data< self.minEle:
				print("pushed element is ", (2*data-self.minEle))	
				self.items.append((2*data) - self.minEle)
				self.minEle = data
			print("Min ele ", self.minEle)
	
	def pop(self):
		y = self.items.pop()
		min = self.minEle
		if y>= min:
			specialStack.setMin(self, min)
			#self.minEle = min
		elif (y<min):
			specialStack.setMin(self, ((2*min)-y))
			#self.minEle  = ((2*min)- y)
		return self.items.pop()
	
	def getMin(self):
		return self.minEle

#	def printStack(self):

#	****

ss = specialStack()
ss.push(3)
print("Initial minimum ", ss.getMin())

ss.push(5)		
print("Minimum second ", ss.getMin())

ss.push(2)
ss.push(1)
print(ss.pop())
print(ss.pop())
print(ss.pop())
#print(ss.pop())
#print("Third minimum ", ss.getMin())

#ss.push(1)
#ss.push(-1)
#print("Fourth minimum", ss.getMin())

